from django import forms
from .models import Alfajor

class AlfajorForm(forms.ModelForm):
    class Meta:
        model = Alfajor
        fields = ["nombre", "categoria", "relleno", "precio","imagen","activo"]