"""Entrega1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.contrib import admin
from django.urls import include, path
from Apps_Entrega1.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/'    , admin.site.urls),
    path('', index, name='index'),  #al no poner nada, se carga el index.html cuando abres la pagina
    path("ingresar/", form_ingresar_usuario, name="form_ingresar_usuario"),
    path("form_crear_usuario/", crear_usuario, name="form_crear_usuario"),
    path('salir', LogoutView.as_view(next_page="/ingresar"), name='salir'),
    path("recuperar/", form_recuperar_usuario, name="form_recuperar_usuario"),
    path("buscar/"   , buscar,    name="buscar"),
    path("teatro/"   , teatro,    name="teatro"),
    path("deporte/"  , deporte,   name="deporte"),
    path("peliculasFormulario/", peliculasFormulario, name="peliculasFormulario"),
    path("teatroFormulario/", teatroFormulario, name="teatroFormulario"),
    path("deporteFormulario/", deporteFormulario, name="deporteFormulario"),
    path("busquedaPelicula/", busquedaPelicula, name="busquedaPelicula"),
    path("buscar/", buscar, name="buscar"),
]