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

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User




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
    username = forms.CharField(max_length=30, required=True, help_text='Requerido. 30 caracteres o menos. Letras, dígitos y @/./+/-/_ solamente.')  
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    password1 = forms.CharField(label='Ingrese la contraseña', max_length=100, widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirme la contraseña', max_length=100, widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}




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