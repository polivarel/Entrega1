from django.shortcuts import render
from django.http import HttpResponse
from random import *
from django.template import loader

def inicio(request):
   mymembers = {'saludo':"Hola"}#"Members.objects.all().values()"
   #template = get_template("IngresarPelicula.html") 
   template = loader.get_template('ingresar_pelicula.html')
   context = {
   'mymembers': mymembers,
   }
   return HttpResponse(template.render(context, request))

def ingresar_pelicula(request):
   mymembers = {'saludo':"Hola"}#"Members.objects.all().values()"
   #template = get_template('IngresarPelicula.html')
   template = loader.get_template('ingresar_pelicula.html')
   context = {
   'mymembers': mymembers,
   }
   return HttpResponse(template.render(context, request))

def ingresar_teatro(request):
    mymembers = {'saludo':"Hola"}#"Members.objects.all().values()"
    template1 = loader.get_template('ingresar_teatro.html')
    context = {
    'mymembers': mymembers,
    }
    return HttpResponse(template1.render(context, request))

def ingresar_deporte(request):
    mymembers = {'saludo':"Hola"}#"Members.objects.all().values()"
    template2 = loader.get_template('ingresar_deporte.html')
    context = {
    'mymembers': mymembers,
    }
    return HttpResponse(template2.render(context, request))