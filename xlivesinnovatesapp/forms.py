from django import forms
from .models import FishPond

class FishPondForm(forms.ModelForm):
    class Meta:
        model = FishPond
        fields = '__all__'
