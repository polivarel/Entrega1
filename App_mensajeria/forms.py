from logging import PlaceHolder
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import Form, HiddenInput, CharField, ChoiceField, ModelForm

from typing import Any, Dict, Iterable, List, Optional, Type, TypeVar, Union
from unittest.util import _MAX_LENGTH

import datetime

from django.contrib.auth.decorators import login_required
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.core.exceptions import ValidationError
from django.db import models
#from django.forms.fields import _ClassLevelWidgetT
from django.forms.widgets import Widget
from django.http.request import HttpRequest
#from App_mensajeria import mensajes_db




UserModel: Type[AbstractBaseUser]
_User = TypeVar("_User", bound=AbstractBaseUser)


#===============================================================================
#=========================== FORMULARIOS DEL USUARIO ===========================

    
#@login_required
class form_verMensajes(forms.ModelForm):
    first_name = forms.CharField( label='Nombre'   ,max_length=30, required=False, widget=forms.TextInput(attrs= {'title':'Escriba su nombre.'}))
    last_name  = forms.CharField( label='Apellido' ,max_length=30, required=False, widget=forms.TextInput(attrs= {'title':'Escriba su apellido'}))   
    username   = forms.CharField( label='Usuario'  ,max_length=30, required=True , widget=forms.TextInput(attrs= {'title':'Requerido. 30 caracteres o menos. Letras, dígitos y @/./+/-/_ solamente.'}))  
    email      = forms.EmailField(label='Correo'   ,max_length=254,required=True , widget=forms.EmailInput(attrs={'title':'Requerido. Ingrese una dirección de correo electrónico válida.'}))
    
    class Meta:
        model = User
        fields = ['first_name','last_name','username', 'email' ]

"""     def clean_email(self):
        email = self.cleaned_data.get('email')
        if email and User.objects.filter(email=email).exclude(username=self.instance.username).exists():
            raise forms.ValidationError('El correo ya existe')
        return email
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if username and User.objects.filter(username=username).exclude(username=self.instance.username).exists():
            raise forms.ValidationError('El usuario ya existe')
        return username   """  


class Form_mensajeAa(forms.Form):
    mensaje     = forms.CharField(label='')
    propietario = forms.HiddenInput()
    receptor    = forms.HiddenInput()

    #class Meta:
    #    model = forms
    #    fields = ['mensaje','propietario']

class Form_casilla(forms.Form):
    id          = forms.CharField()
    propietario = forms.CharField()
    receptor    = forms.CharField()
    mensaje     = forms.CharField()
    fecha       = forms.DateTimeField()
    hora        = forms.TimeField()
#===============================================================================
#=========================== FORMULARIOS DEL USUARIO ===========================














