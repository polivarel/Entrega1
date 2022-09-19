from logging import PlaceHolder
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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





UserModel: Type[AbstractBaseUser]
_User = TypeVar("_User", bound=AbstractBaseUser)


#===============================================================================
#=========================== FORMULARIOS DEL USUARIO ===========================
class AuthenticationForm(forms.Form):
    username: forms.Field = ...
    password: forms.Field = ...
    #error_messages: _ErrorMessagesT = ...
    request: Optional[HttpRequest] = ...
    user_cache: Any = ...
    username_field: models.Field = ...
    def __init__(self, request: Optional[HttpRequest] = ..., *args: Any, **kwargs: Any) -> None: ...
    def confirm_login_allowed(self, user: AbstractBaseUser) -> None: ...
    def get_user(self) -> AbstractBaseUser: ...
    def get_invalid_login_error(self) -> ValidationError: ...
    def clean(self) -> Dict[str, Any]: ...

class form_recuperar_usuario(forms.Form):
    correo = forms.EmailField()

#@login_required
class form_crear_usuario(UserCreationForm):
    first_name = forms.CharField( label='Nombre'                ,max_length=30, required=False, widget=forms.TextInput(attrs= {'title':'Escriba su nombre.'}))
    last_name  = forms.CharField( label='Apellido'              ,max_length=30, required=False, widget=forms.TextInput(attrs= {'title':'Escriba su apellido'}))   
    username   = forms.CharField( label='Usuario'               ,max_length=30, required=True , widget=forms.TextInput(attrs= {'title':'Requerido. 30 caracteres o menos. Letras, dígitos y @/./+/-/_ solamente.'}))  
    email      = forms.EmailField(label='Correo'                ,max_length=254,required=True , widget=forms.EmailInput(attrs={'title':'Requerido. Ingrese una dirección de correo electrónico válida.'}))
    password1  = forms.CharField( label='Ingrese la contraseña' ,max_length=100, widget=forms.PasswordInput)
    password2  = forms.CharField( label='Confirme la contraseña',max_length=100, widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['first_name','last_name','username', 'email', 'password1', 'password2']
    

class form_editar_usuarios(forms.Form):
    id         = forms.IntegerField(widget=forms.HiddenInput())
    first_name = forms.CharField( label='Nombre'                ,max_length=30, required=False, widget=forms.TextInput(attrs= {'title':'Escriba su nombre.'}))
    last_name  = forms.CharField( label='Apellido'              ,max_length=30, required=False, widget=forms.TextInput(attrs= {'title':'Escriba su apellido'}))   
    username   = forms.CharField( label='Usuario'               ,max_length=30, required=True , widget=forms.TextInput(attrs= {'title':'Requerido. 30 caracteres o menos. Letras, dígitos y @/./+/-/_ solamente.'}))  
    email      = forms.EmailField(label='Correo'                ,max_length=254,required=True , widget=forms.EmailInput(attrs={'title':'Requerido. Ingrese una dirección de correo electrónico válida.'}))
      
    class Meta:
        model = User
        fields = ['id','first_name','last_name','username', 'email' ]


#===============================================================================
#=========================== FORMULARIOS DEL USUARIO ===========================














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