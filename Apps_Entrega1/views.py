import re
from django.shortcuts import render
from django.http import HttpResponse
from random import *
from django.template import loader
from Apps_Entrega1.forms import *
from Apps_Entrega1.models import *

def index(request):
    mymembers = {'saludo':"Hola"}#"Members.objects.all().values()"
    template2 = loader.get_template('index.html')
    context = {
    'mymembers': mymembers,
    }
    return HttpResponse(template2.render(context, request))

#def buscar(request):
    #mymembers = {'saludo':"Hola"}#"Members.objects.all().values()"
    #template2 = loader.get_template('buscar.html')
    #context = {
    #'mymembers': mymembers,
    #}
    #return HttpResponse(template2.render(context, request))

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


def peliculasFormulario(request):
    if request.method=="POST":
        form=PeliForm(request.POST)
        if form.is_valid():
            informacion=form.cleaned_data
            titulo=informacion["titulo"]
            lugar=informacion["lugar"]
            pelicula=Peliculas(titulo=titulo, lugar=lugar)
            pelicula.save()
            return render (request, "index.html")
    else:
        formulario=PeliForm()
        return render (request, "peliculasFormulario.html", {"formulario":formulario})

def teatroFormulario(request):
    if request.method=="POST":
        form=TeatroForm(request.POST)
        if form.is_valid():
            informacion=form.cleaned_data
            titulo=informacion["titulo"]
            lugar=informacion["lugar"]
            obra=Teatro(titulo=titulo, lugar=lugar)
            obra.save()
            return render (request, "index.html")
    else:
        formulario=TeatroForm()
        return render (request, "teatroFormulario.html", {"formulario":formulario})

def deporteFormulario(request):
    if request.method=="POST":
        form=DeporteForm(request.POST)
        if form.is_valid():
            informacion=form.cleaned_data
            titulo=informacion["titulo"]
            lugar=informacion["lugar"]
            partido=Deporte(titulo=titulo, lugar=lugar)
            partido.save()
            return render (request, "index.html")
    else:
        formulario=DeporteForm()
        return render (request, "deporteFormulario.html", {"formulario":formulario})

def busquedaPelicula(request):
    return render(request, "busquedaPelicula.html")

def buscar(request):
    if request.GET["titulo"]:
        titulo=request.GET["titulo"]
        peliculas=Peliculas.objects.filter(titulo=titulo)
        return render(request, "resultadosBusqueda.html", {"peliculas":peliculas})
    else:
        return render(request, "busquedaPelicula.html", {"mensaje":"Ingrese una pelicula"})