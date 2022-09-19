from django.contrib import admin
from django.urls import include, path
from Apps_Entrega1.views import *
from django.contrib.auth.views import LogoutView
#linea reservada para Pablo
#linea reservada para Pablo
#linea reservada para Pablo
#linea reservada para Pablo





urlpatterns = [
    path('admin/'    , admin.site.urls),
    path('', index, name='index'),  #al no poner nada, se carga el index.html cuando abres la pagina editar_usuarios
    path("ingresar/", form_ingresar_usuario, name="form_ingresar_usuario"),
    path("form_crear_usuario/", crear_usuario, name="form_crear_usuario"),
    path('salir', LogoutView.as_view(next_page="/ingresar"), name='salir'),
    path("listar_usuarios/", listar_usuarios, name="listar_usuarios"),
    path("editar_usuarios/", editar_usuarios, name="form_editar_usuarios"),
    #linea reservada para Pablo
    #linea reservada para Pablo
    #linea reservada para Pablo
    path("buscar/"   , buscar,    name="buscar"),
    path("teatro/"   , teatro,    name="teatro"),
    path("deporte/"  , deporte,   name="deporte"),
    path("peliculasFormulario/", peliculasFormulario, name="peliculasFormulario"),
    path("teatroFormulario/", teatroFormulario, name="teatroFormulario"),
    path("deporteFormulario/", deporteFormulario, name="deporteFormulario"),
    path("busquedaPelicula/", busquedaPelicula, name="busquedaPelicula"),
    path("buscar/", buscar, name="buscar"),
]