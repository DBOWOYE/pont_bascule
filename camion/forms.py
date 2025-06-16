from django import forms
from .models import *

class CamionForm(forms.ModelForm):
    class Meta:
        model = Camion
        fields = ('radar', 'immatriculation', 'partenaire')