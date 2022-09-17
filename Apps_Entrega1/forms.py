#from socket import fromshare
from unittest.util import _MAX_LENGTH
from django import forms
import datetime

class formIngresarUsuario(forms.Form):
    usuario = forms.CharField()
    clave   = forms.CharField()


class PeliForm(forms.Form):
    fecha_inicio = forms.DateField(initial=datetime.date.today, widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    lugar        = forms.CharField(max_length=50)
    titulo       = forms.CharField(max_length=180)
    hora_inicio  = forms.TimeField( widget=forms.widgets.DateInput(attrs={'type': 'time'}))
    edad_minima  = forms.DecimalField(min_value=1)
    puntaje      = forms.DecimalField(min_value=1,max_value=100)



class TeatroForm(forms.Form):
    titulo = forms.CharField(max_length=180)
    lugar  = forms.CharField(max_length=50)

class DeporteForm(forms.Form):
    titulo = forms.CharField(max_length=180)
    lugar  = forms.CharField(max_length=50)