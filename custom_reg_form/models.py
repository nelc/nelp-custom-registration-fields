from django.conf import settings
from django.db import models

# Backwards compatible settings.AUTH_USER_MODEL
USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')


class ExtraInfo(models.Model):
    """
    This model contains one extra field that will be saved when a user registers.
    The form that wraps this model is in the forms.py file.
    """
    user = models.OneToOneField(USER_MODEL, on_delete=models.CASCADE, null=True)

    arabic_name = models.CharField(max_length=255)

    allow_newsletter_emails = models.BooleanField(default=False, blank=True)

    def __str__(self):
        return "[{user_id}] {username} - {arabic_name}".format(
            user_id=self.user.id,
            username=self.user.username,
            arabic_name=self.arabic_name
        )
