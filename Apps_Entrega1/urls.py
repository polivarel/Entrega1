from django.urls import path
from Apps_Entrega1.views import *

urlpatterns = [
    path("", inicio, name="inicio"),
    path("peliculas/", peliculas, name="peliculas"),
    #path("ingresar_pelicula/", ingresar_pelicula),
    path("teatro/", teatro, name="teatro"),
    #path("ingresar_teatro/", ingresar_teatro),
    path("deporte/", deporte, name="deporte"),
    #path("ingresar_deporte/", ingresar_deporte),
]