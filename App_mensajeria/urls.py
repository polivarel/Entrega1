from django.contrib import admin
from django.urls import include, path

from django.contrib.auth.views import LogoutView
from Apps_Entrega1.views import *
from App_mensajeria.views import *

#linea reservada para Pablo
#linea reservada para Pablo
#linea reservada para Pablo
#linea reservada para Pablo





urlpatterns = [
    path('admin/'    , admin.site.urls),
    path('', index, name='index'),  
    
    path("mensajes/", verMensajes , name="verMensajes"),
    path("mensajeA/<int:id>", mensajeA , name="Form_mensajeA"),



]