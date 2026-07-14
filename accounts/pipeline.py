import logging
 
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.shortcuts import redirect
 
from .models import Profile
 
logger = logging.getLogger(__name__)
User = get_user_model()
 
 
def check_existing_email(strategy, details, user=None, *args, **kwargs):
    """
    Runs right before create_user. If this social login has no existing
    association yet (user is None) and a *verified* local account
    already owns this email, stop the pipeline and send the person to
    the login page with an explanation, instead of silently creating a
    second, disconnected account for the same person.
 
    An existing but never-verified account (abandoned OTP signup) is
    treated differently: Google has just proven real ownership of the
    email, which is at least as strong as our own OTP check ever was,
    so we clear the stale row and let the pipeline continue normally.
    """
    if user is not None:
        return  
    
    email = details.get("email")
    if not email:
        return
 
    existing = User.objects.filter(email__iexact=email).first()
    if existing is None:
        return
 
    if not existing.is_active:
        existing.delete()
        logger.info("Cleared stale unverified account for %s before social signup", email)
        return
 
    request = strategy.request
    messages.warning(
        request,
        "An account with this email already exists. Sign in with your "
        "password instead, or use \"Forgot password\" if you don't remember it.",
    )
    logger.info("Blocked social signup for existing verified email: %s", email)
    return redirect("login")
 
 
def create_profile(strategy, user, *args, **kwargs):
    """
    Create the user's Profile the moment a social-auth account is created.
    """
    if user is None:
        return
    Profile.objects.get_or_create(user=user)
 