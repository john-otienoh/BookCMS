import logging

from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.contrib.auth.decorators import login_required
from django.core.cache import cache
from django.core.mail import send_mail
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.views.decorators.http import require_POST

from .forms import EmailAuthenticationForm, OTPVerificationForm, ProfileEditForm, SignUpForm
from .models import EmailOTP, Profile
from .signals import user_verified

logger = logging.getLogger(__name__)
User = get_user_model()

OTP_RESEND_COOLDOWN = 60     
OTP_MAX_ATTEMPTS = 5            
OTP_LOCKOUT_SECONDS = 300
LOGIN_MAX_ATTEMPTS = 5
LOGIN_LOCKOUT_SECONDS = 300


def _client_ip(request):
    return request.META.get("REMOTE_ADDR")


def _send_verification_email(user, otp, request):
    """Email both the 6-digit code and a one-click verification link."""
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    verify_url = request.build_absolute_uri(
        reverse("register_confirm_link", kwargs={"uidb64": uid, "token": otp.token})
    )
    subject = "Verify your email address"
    message = render_to_string(
        "accounts/email/verification_email.txt",
        {"user": user, "code": otp.code, "verify_url": verify_url},
    )
    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [user.email], fail_silently=False)


def _activate_user(request, user, otp):
    otp.mark_used()
    user.is_active = True
    user.save(update_fields=["is_active"])
    request.session.pop("pending_user_id", None)
    user.backend = "accounts.backends.EmailBackend"
    login(request, user)
    user_verified.send(sender=user.__class__, user=user)
    logger.info("User %s verified and logged in from %s", user.email, _client_ip(request))
    messages.success(request, "Your email has been verified. Welcome!")


# --- Registration -----------------------------------------------------

def signup_view(request):
    if request.user.is_authenticated:
        return redirect("profile")

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            otp = EmailOTP.objects.create(user=user, purpose=EmailOTP.PURPOSE_SIGNUP)
            _send_verification_email(user, otp, request)
            request.session["pending_user_id"] = user.pk
            logger.info("New signup pending verification: %s", user.email)
            return redirect("register_done")
    else:
        form = SignUpForm()

    return render(request, "accounts/register.html", {"form": form})


def register_done_view(request):
    return render(request, "accounts/register_done.html")


def register_confirm_view(request):
    """Manual path: user types the 6-digit code they received by email."""
    pending_id = request.session.get("pending_user_id")
    user = User.objects.filter(pk=pending_id, is_active=False).first() if pending_id else None

    if user is None:
        messages.error(request, "Your verification session has expired. Please sign up again.")
        return redirect("register")

    if request.method == "POST":
        attempts_key = f"otp_attempts:{user.pk}"
        if cache.get(attempts_key, 0) >= OTP_MAX_ATTEMPTS:
            messages.error(request, "Too many incorrect attempts. Request a new code and try again.")
            return render(request, "accounts/register_confirm.html", {"form": OTPVerificationForm(), "validlink": True})

        form = OTPVerificationForm(request.POST)
        if form.is_valid():
            code = form.cleaned_data["code"]
            otp = EmailOTP.objects.filter(
                user=user, code=code, purpose=EmailOTP.PURPOSE_SIGNUP, is_used=False
            ).first()
            if otp and otp.is_valid():
                cache.delete(attempts_key)
                _activate_user(request, user, otp)
                return redirect("profile")

            cache.set(attempts_key, cache.get(attempts_key, 0) + 1, timeout=OTP_LOCKOUT_SECONDS)
            form.add_error("code", "That code is invalid or has expired.")
    else:
        form = OTPVerificationForm()

    return render(request, "accounts/register_confirm.html", {"form": form, "validlink": True})


def register_confirm_link_view(request, uidb64, token):
    """Link path: user clicked the emailed magic link."""
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (User.DoesNotExist, ValueError, TypeError, OverflowError):
        user = None

    otp = None
    if user is not None:
        otp = EmailOTP.objects.filter(user=user, token=token, purpose=EmailOTP.PURPOSE_SIGNUP).first()

    if user is not None and otp is not None and otp.is_valid():
        _activate_user(request, user, otp)
        return redirect("profile")

    messages.error(request, "This verification link is invalid or has expired.")
    return render(
        request,
        "accounts/register_confirm.html",
        {"form": OTPVerificationForm(), "validlink": False},
    )


@require_POST
def resend_otp_view(request):
    pending_id = request.session.get("pending_user_id")
    user = User.objects.filter(pk=pending_id, is_active=False).first() if pending_id else None
    if user is None:
        messages.error(request, "Nothing to resend — please sign up again.")
        return redirect("register")

    cooldown_key = f"otp_resend:{user.pk}"
    if cache.get(cooldown_key):
        messages.warning(request, "Please wait a moment before requesting another code.")
        return redirect("register_confirm")

    EmailOTP.objects.filter(user=user, purpose=EmailOTP.PURPOSE_SIGNUP, is_used=False).update(is_used=True)
    otp = EmailOTP.objects.create(user=user, purpose=EmailOTP.PURPOSE_SIGNUP)
    _send_verification_email(user, otp, request)
    cache.set(cooldown_key, True, timeout=OTP_RESEND_COOLDOWN)
    messages.success(request, "A new code has been sent to your email.")
    return redirect("register_confirm")


# --- Session auth -------------------------------------------------------

def signin_view(request):
    if request.user.is_authenticated:
        return redirect("profile")

    if request.method == "POST":
        form = EmailAuthenticationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]

            lockout_key = f"login_attempts:{email.lower()}"
            if cache.get(lockout_key, 0) >= LOGIN_MAX_ATTEMPTS:
                form.add_error(None, "Too many failed attempts. Please try again in a few minutes.")
                return render(request, "accounts/login.html", {"form": form})

            user = authenticate(request, email=email, password=password)
            if user is not None:
                cache.delete(lockout_key)
                login(request, user)
                logger.info("User %s signed in from %s", user.email, _client_ip(request))
                next_url = request.POST.get("next") or request.GET.get("next") or reverse("profile")
                return redirect(next_url)

            cache.set(lockout_key, cache.get(lockout_key, 0) + 1, timeout=LOGIN_LOCKOUT_SECONDS)
            logger.warning("Failed sign-in attempt for %s from %s", email, _client_ip(request))

            if User.objects.filter(email__iexact=email, is_active=False).exists():
                form.add_error(None, "Please verify your email before signing in.")
            else:
                form.add_error(None, "Invalid email or password.")
    else:
        form = EmailAuthenticationForm()

    return render(request, "accounts/login.html", {"form": form})


def signout_view(request):
    logout(request)
    return render(request, "accounts/logout.html")


# --- Profile --------------------------------------------------------------

@login_required
def profile_view(request):
    profile, _ = Profile.objects.get_or_create(user=request.user)
    return render(request, "accounts/profile.html", {"profile": profile})


@login_required
def profile_edit_view(request):
    profile, _ = Profile.objects.get_or_create(user=request.user)

    if request.method == "POST":
        form = ProfileEditForm(request.POST, request.FILES, instance=profile, user=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully.")
            return redirect("profile")
    else:
        form = ProfileEditForm(instance=profile, user=request.user)

    return render(request, "accounts/profile_edit.html", {"form": form})
