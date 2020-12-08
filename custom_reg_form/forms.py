import re

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _
from .models import ExtraInfo
from django.forms import ModelForm


class ExtraInfoForm(ModelForm):
    """
    The fields on this form are derived from the ExtraInfo model in models.py.
    """

    class Meta(object):
        model = ExtraInfo
        fields = ('arabic_name', 'allow_newsletter_emails',)
        labels = {
            'allow_newsletter_emails': _("I agree to receive newsletters, or marketing and promotional content")
        }

    def _validate_arabic_name(self, arabic_name):
        """Check if the name has characters other than arabic."""
        if re.findall(u'[^\u0600-\u06ff\W]', arabic_name, flags=re.UNICODE):
            msg = "Arabic Name field can accept only arabic characters."
            raise ValidationError(msg)

    def clean_arabic_name(self):
        """Validate the field should have just arabic characters."""
        arabic_name = self.cleaned_data['arabic_name']
        self._validate_arabic_name(arabic_name)
        return arabic_name
