import re
from django.shortcuts import render
from django.http import HttpResponse
from random import *
from django.template import loader
from Apps_Entrega1.forms import *

def index(request):
    mymembers = {'saludo':"Hola"}#"Members.objects.all().values()"
    template2 = loader.get_template('index.html')
    context = {
    'mymembers': mymembers,
    }
    return HttpResponse(template2.render(context, request))

def buscar(request):
    mymembers = {'saludo':"Hola"}#"Members.objects.all().values()"
    template2 = loader.get_template('buscar.html')
    context = {
    'mymembers': mymembers,
    }
    return HttpResponse(template2.render(context, request))

def deporte(request):
    mymembers = {'saludo':"Hola"}#"Members.objects.all().values()"
    template2 = loader.get_template('deporte.html')
    context = {
    'mymembers': mymembers,
    }
    return HttpResponse(template2.render(context, request))

def ok(request):
    mymembers = {'saludo':"Hola"}#"Members.objects.all().values()"
    template1 = loader.get_template('ok.html')
    context = {
    'mymembers': mymembers,
    }
    return HttpResponse(template1.render(context, request))


def teatro(request):
    mymembers = {'saludo':"Hola"}#"Members.objects.all().values()"
    template1 = loader.get_template('teatro.html')
    context = {
    'mymembers': mymembers,
    }
    return HttpResponse(template1.render(context, request))

# def peliculas(request):
#     mymembers = {'saludo':"Hola"}#"Members.objects.all().values()"
#     template1 = loader.get_template('peliculas.html')
#     context = {
#     'mymembers': mymembers,
#     }
#     return HttpResponse(template1.render(context, request))

def peliculas(request):
    if request.method == 'POST':
        FormPelicula = IngPeli(request.POST)
        print(FormPelicula)
        if FormPelicula.is_valid:
            informacion = FormPelicula.cleaned_data
            peli = IngPeli(fecha_inicio=informacion['fecha_inicio'],lugar=informacion['lugar'],titulo=informacion['titulo'],hora_inicio=informacion['hora_inicio'],edad_minima=informacion['edad_minima'],puntaje=informacion['puntaje'])
            peli.save()
            return render(request,"App_Entrega1/test.html")
    else:
        FormPelicula=FormPelicula()
    return render(request, "App_Entrega1/peliculas.html",{})    