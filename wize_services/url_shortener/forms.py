from django import forms
from .models import UrlShort


class UrlConvertForm(forms.ModelForm):

    class Meta:
        model = UrlShort
        fields = [
            'long_url',
        ]

    def __init__(self, *args, **kwargs):
        super(UrlConvertForm, self).__init__(*args, **kwargs)
        self.fields['long_url'].required = True
