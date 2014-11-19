from django import forms

from .models import SummonerInput

class SummonerInputForm(forms.ModelForm):
    class Meta:
        model = SummonerInput