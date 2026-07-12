from django.dispatch import Signal, receiver

from .models import Profile
user_verified = Signal()  

@receiver(user_verified)
def create_profile_on_verification(sender, user, **kwargs):
    """
    Create the user's Profile only once they're confirmed as a real,
    verified account — not the moment they merely submit the signup
    form. get_or_create keeps this safe to call more than once (e.g.
    for accounts created directly via createsuperuser, which never
    pass through the OTP flow at all).
    """
    Profile.objects.get_or_create(user=user)

