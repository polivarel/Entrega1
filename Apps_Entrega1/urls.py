from django.contrib import admin
from django.urls import path
from Clase18.views import *
from Apps_Clase18.views import crearRandom

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ingresar_pelicula/', ingresar_pelicula),
]