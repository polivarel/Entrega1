from django.shortcuts import render

from pydoc import visiblename
from django.shortcuts import render, redirect
from django.http import HttpResponse

from random import *
from django.template import loader
from App_mensajeria.forms import *
from App_mensajeria.models import *

#from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy    

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth import login, logout, authenticate, get_user_model

from django.contrib.auth.decorators import login_required
from django.db.models import Q


def verMensajes(request):
    logeado = request.session['logeado'] = request.user.username
    usuarios = User.objects.all()
    return render(request, "mensajes/listar.html", {"usuarios":usuarios,"logeado":logeado})

def mensajeA(request,id):
    receptor = User.objects.get(id=id)
    if request.method == 'POST':
        form = Form_mensajeAa(request.POST)
        if form.is_valid():
            info= form.cleaned_data
            mensaje= info["mensaje"]
            receptor = receptor.username
            propietario = request.user
            msj= mensajes_db(mensaje=mensaje,receptor=receptor,propietario=propietario)
            msj.save()
            return redirect('Form_mensajeA',id)
        else:
            return render(request, "mensajes/enviar.html", {"formulario_casilla":form})    
    else:
        form = Form_mensajeAa()
        logeado = request.session.get('logeado')
        mensajes_todos = mensajes_db.objects.filter(
        Q(propietario=logeado,receptor=receptor) | Q(propietario=receptor,receptor=logeado)
        )
        return render(request, 'mensajes/enviar.html', {'formulario_casilla': form,"destino":receptor,"id_destino":id,"mensajes":mensajes_todos})




def verCasilla(request):
    form = Form_casilla()
    #mensajes_todos = mensajes_db.objects.filter(propietario="jpalotes",receptor="pablo").filter(propietario="pablo",receptor="jpalotes")
    #mensajes_todos = mensajes_db.objects.filter(propietario="pablo",receptor="jpalotes")
    mensajes_todos = mensajes_db.objects.filter(
    Q(propietario="jpalotes",receptor="pablo") | Q(propietario="pablo",receptor="jpalotes")
    )
    return render(request, 'mensajes/mensajes.html', {'formulario_mensajes': form,"mensajes":mensajes_todos})


def contenido(request,id):
    receptor = User.objects.get(id=id)
    form = Form_mensajeAa()
    logeado = request.session.get('logeado')
    mensajes_todos = mensajes_db.objects.filter(
    Q(propietario=logeado,receptor=receptor) | Q(propietario=receptor,receptor=logeado)
    )
    return render(request, "mensajes/contenido_mensajes.html", {'formulario_mensajes': form,"mensajes":mensajes_todos})