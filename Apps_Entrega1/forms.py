from logging import PlaceHolder
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from typing import Any, Dict, Iterable, List, Optional, Type, TypeVar, Union
from unittest.util import _MAX_LENGTH

from datetime import datetime

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
    
#@login_required
class form_editar_usuarios(forms.ModelForm):
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




class form_eliminar_usuario(forms.ModelForm):
    id = forms.IntegerField(widget=forms.HiddenInput())
    username = forms.CharField(label='Usuario', widget=forms.TextInput(attrs={'readonly':'readonly'}))
    class Meta:
        model = User
        fields = ['id','username']


#===============================================================================
#=========================== FORMULARIOS DEL USUARIO ===========================



class EventoForm(forms.Form):
    propietario=forms.CharField()
    titulo=forms.CharField()
    subtitulo=forms.CharField()
    cuerpo=forms.CharField(widget=forms.Textarea)
    autor=forms.CharField()
    fecha=forms.DateField()
    imagen=forms.ImageField()
    