import re
from django.shortcuts import render
from django.http import HttpResponse
from random import *
from django.template import loader
from Apps_Entrega1.forms import *
from Apps_Entrega1.models import *
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate


from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

def index(request):
    mymembers = {'saludo':"Hola"}#"Members.objects.all().values()"
    template2 = loader.get_template('index.html')
    context = {
    'mymembers': mymembers,
    }
    return HttpResponse(template2.render(context, request))

            
def form_ingresar_usuario(request):
    if request.method=="POST":
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usu=request.POST["username"]
            clave=request.POST["password"]

            usuario=authenticate(username=usu, password=clave)
            if usuario is not None:
                login(request, usuario)
                return render(request, '00usuario_ingresar.html', {'mensaje':f"Bienvenido {usuario}"})
            else:
                return render(request, "00usuario_ingresar.html", {"formulario":form, "mensaje":"Usuario o contraseña incorrectos"})
        else:
            return render(request, "00usuario_ingresar.html", {"formulario":form, "mensaje":"Usuario o contraseña incorrectos"})
                
    else:
        form=AuthenticationForm()
        return render(request, "00usuario_ingresar.html", {"formulario":form})












def deporte(request):
    mymembers = {'saludo':"Hola"}#"Members.objects.all().values()"
    template2 = loader.get_template('deporte.html')
    context = {
    'mymembers': mymembers,
    }
    return HttpResponse(template2.render(context, request))


def teatro(request):
    mymembers = {'saludo':"Hola"}#"Members.objects.all().values()"
    template1 = loader.get_template('teatro.html')
    context = {
    'mymembers': mymembers,
    }
    return HttpResponse(template1.render(context, request))

def peliculasFormulario(request):
    if request.method=="POST":
        form=PeliForm(request.POST)
        if form.is_valid():
            informacion=form.cleaned_data
            fecha_inicio=informacion["fecha_inicio"]
            lugar=informacion["lugar"]
            titulo=informacion["titulo"]
            hora_inicio=informacion["hora_inicio"]
            edad_minima=informacion["edad_minima"]
            puntaje=informacion["puntaje"]
            pelicula=Peliculas(fecha_inicio=fecha_inicio,lugar=lugar,titulo=titulo, hora_inicio=hora_inicio,edad_minima=edad_minima,puntaje=puntaje)
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