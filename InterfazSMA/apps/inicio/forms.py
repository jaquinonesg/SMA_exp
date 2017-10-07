from .models import *
from django import forms

class AgenteForm(forms.ModelForm):
    class Meta:
        model = Agente
        fields = ['nombre', 'estado', 'transicion']
