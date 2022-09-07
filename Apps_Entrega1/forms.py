from socket import fromshare
from django import forms

#class IngPeli(forms.Form):
   # fecha_inicio = forms.CharField()
   # lugar        = forms.CharField()
    #titulo       = forms.CharField()
    #hora_inicio  = forms.CharField()
    #edad_minima  = forms.CharField()
   # puntaje      = forms.CharField()

class PeliForm(forms.Form):
    titulo = forms.CharField(max_length=180)
    lugar = forms.CharField(max_length=50)

class TeatroForm(forms.Form):
    titulo = forms.CharField(max_length=180)
    lugar = forms.CharField(max_length=50)

class DeporteForm(forms.Form):
    titulo = forms.CharField(max_length=180)
    lugar = forms.CharField(max_length=50)