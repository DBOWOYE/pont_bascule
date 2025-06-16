from django import forms
from .models import Pesee

class PeseeForm(forms.ModelForm):
    class Meta:
        model = Pesee
        fields = ('camion','poids_vide', 'poids_charge')

