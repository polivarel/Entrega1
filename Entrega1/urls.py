from django.contrib import admin
from django.urls import include, path

from django.contrib.auth.views import LogoutView
from Apps_Entrega1.views import *

from django.conf import settings #add this
from django.conf.urls.static import static #add this
#linea reservada para Pablo
#linea reservada para Pablo
#linea reservada para Pablo
#linea reservada para Pablo





urlpatterns = [
    path('admin/'    , admin.site.urls),
    path('', index, name='index'),  
    # path("buscar/", buscar, name="buscar"),

    path('App_mensajeria/', include('App_mensajeria.urls')),

    path("ingresar/", form_ingresar_usuario, name="form_ingresar_usuario"),
    path("form_crear_usuario/", crear_usuario, name="form_crear_usuario"),
    path('salir', LogoutView.as_view(next_page="/"), name='salir'),
    path("listar_usuarios/", listar_usuarios, name="listar_usuarios"),
    path("editar_usuarios/<int:id>", editar_usuarios, name="form_editar_usuarios"),
    path("listar_usuarios/", listar_usuarios, name="listar_usuarios"),
    path("eliminar_usuario/<int:id>", eliminar_usuario, name="form_eliminar_usuario"),



    path("eventoFormulario/", evento, name="evento_Formulario"),



]
if settings.DEBUG: #add this
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
