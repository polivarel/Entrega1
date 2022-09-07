from django.shortcuts import render
from django.http import HttpResponse
from random import *
from django.template import loader


def index(request):
    mymembers = {'saludo':"Hola"}#"Members.objects.all().values()"
    template2 = loader.get_template('index.html')
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


def teatro(request):
    mymembers = {'saludo':"Hola"}#"Members.objects.all().values()"
    template1 = loader.get_template('teatro.html')
    context = {
    'mymembers': mymembers,
    }
    return HttpResponse(template1.render(context, request))

def peliculas(request):
    mymembers = {'saludo':"Hola"}#"Members.objects.all().values()"
    template1 = loader.get_template('peliculas.html')
    context = {
    'mymembers': mymembers,
    }
    return HttpResponse(template1.render(context, request))
