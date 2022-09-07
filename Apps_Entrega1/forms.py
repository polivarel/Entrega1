from socket import fromshare
from django import forms

class IngPeli(forms.Form):
    fecha_inicio = forms.CharField()
    lugar        = forms.CharField()
    titulo       = forms.CharField()
    hora_inicio  = forms.CharField()
    edad_minima  = forms.CharField()
    puntaje      = forms.CharField()

