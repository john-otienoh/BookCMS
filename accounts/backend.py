from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
import logging

logger = logging.getLogger(__name__)

class EmailBackend(ModelBackend):
    """
    Authenticate with email
    """

    def authenticate(self, request, username=None, password=None, **kwargs):
        UserModel = get_user_model()
        email = kwargs.get("email", username)

        if email is None or password is None:
            return None

        try:
            user = UserModel.objects.get(Q(email__iexact=email) | Q(username__iexact=email))
        except UserModel.DoesNotExist:
            UserModel().set_password(password)
            logger.warning("Authentication failed: no user for %s", email)
            return None
        except UserModel.MultipleObjectsReturned:
            logger.error("Multiple users matched email/username %s", email)
            return None

        if user.check_password(password) and self.user_can_authenticate(user):
            logger.info("User %s authenticated successfully", user.email)
            return user

        return None

    def get_user(self, user_id):
        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(pk=user_id)
        except UserModel.DoesNotExist:
            return None
        return user if self.user_can_authenticate(user) else None
