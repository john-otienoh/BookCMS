from django.db import models
import secrets
from datetime import timedelta

from django.conf import settings
from django.utils import timezone
# Create your models here.

def generate_otp_code():
    """Cryptographically secure 6-digit numeric code, zero-padded."""
    return f"{secrets.randbelow(1_000_000):06d}"


def generate_otp_token():
    """URL-safe token used for the one-click magic link."""
    return secrets.token_urlsafe(32)


def default_expiry():
    return timezone.now() + timedelta(minutes=15)

class EmailOTP(models.Model):
    """
    A one-time verification code + magic-link token issued to a user's email address. 
    """

    PURPOSE_SIGNUP = "signup"
    PURPOSE_LOGIN = "login"
    PURPOSE_CHOICES = [
        (PURPOSE_SIGNUP, "Signup Verification"),
        (PURPOSE_LOGIN, "Passwordless Login"),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="email_otps",
    )
    purpose = models.CharField(max_length=20, choices=PURPOSE_CHOICES, default=PURPOSE_SIGNUP)
    code = models.CharField(max_length=6, default=generate_otp_code)
    token = models.CharField(max_length=64, unique=True, default=generate_otp_token, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField(default=default_expiry)
    is_used = models.BooleanField(default=False)

    class Meta:
        indexes = [
            models.Index(fields=["user", "purpose", "is_used"]),
        ]
        ordering = ["-created_at"]

    def is_expired(self):
        return timezone.now() >= self.expires_at

    def is_valid(self):
        return not self.is_used and not self.is_expired()

    def mark_used(self):
        self.is_used = True
        self.save(update_fields=["is_used"])

    def __str__(self):
        return f"{self.get_purpose_display()} OTP for {self.user}"

class Profile(models.Model):
    """User Profile"""

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="profile",
    )
    bio = models.TextField(max_length=500, blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    avatar = models.ImageField(upload_to="avatars/", blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Profile: {self.user}"