from django import forms
from django.core.exceptions import ValidationError

from .models import Effects, LightStrip

class PickForm(forms.Form):
    which_strip = forms.ModelChoiceField(label="Which Strip?", queryset=LightStrip.objects.all())
    which_effect = forms.ModelChoiceField(label="Which Effect?", queryset=Effects.objects.all(), required=False)
    on_off = forms.BooleanField(label="Turn strip on", required=False)