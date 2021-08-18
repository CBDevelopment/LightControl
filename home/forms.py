from django import forms
from django.core.exceptions import ValidationError

from .models import Effects, LightStrip

STRIP_CHOICES = [
    ('stars', 'Star Strip'),
    ('random', 'Random Light String'),
    ('strip', 'Full Strip')
]

class PickForm(forms.Form):
    which_strip = forms.ModelChoiceField(label="Which Strip?", queryset=LightStrip.objects.all())
    which_effect = forms.ModelChoiceField(label="Which Effect?", queryset=Effects.objects.all(), required=False)
    on_off = forms.BooleanField(label="Turn strip on", required=False)

    # def clean(self):
    #     # Check if the On/Off toggle is pressed, and if it is, require an effect be played
    #     pass