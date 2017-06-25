from django.utils.translation import ugettext as _
from django import forms
from constants import SUPPORTED_TESSERACT_LANGUAGES


class UploadImageFileForm(forms.Form):
    language = forms.ChoiceField(label=_('Language'), choices=SUPPORTED_TESSERACT_LANGUAGES)
    # file = forms.FileField()
    file = forms.ImageField(label=_('Picture'))
