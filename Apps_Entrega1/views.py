from email.mime import image
from pydoc import visiblename
from django.shortcuts import render, redirect
from django.http import HttpResponse
from random import *
from django.template import RequestContext , loader
from Apps_Entrega1.forms import *
from Apps_Entrega1.models import *
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy    
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth import login, logout, authenticate, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User



def index(request):
    return render (request, "index.html")
    #mymembers = {'saludo':"Hola"}#"Members.objects.all().values()"
    #template2 = loader.get_template('index.html')
    #context = {
    #'mymembers': mymembers,
    #}
    #return HttpResponse(template2.render(context, request))



#============================================================================================================
#=================== USUARIOS ===============================================================================            
def form_ingresar_usuario(request):
    if request.method=="POST":
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usu=request.POST["username"]
            clave=request.POST["password"]
            usuario=authenticate(username=usu, password=clave)
            if usuario is not None:
                login(request, usuario)
                return render(request, 'usuarios/ingresar.html', {'mensaje':f"{usuario}"})
            else:
                return render(request, "usuarios/ingresar.html", {"formulario":form, "mensaje":"Usuario o contraseña incorrectos"})
        else:
            return render(request, "usuarios/ingresar.html", {"formulario":form, "mensaje":"Usuario o contraseña incorrectos"})
    else:
        form=AuthenticationForm()
        return render(request, "usuarios/ingresar.html", {"formulario":form})


def crear_usuario(request):
    if request.method == 'POST':
        form = form_crear_usuario(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            form.save()
            return render(request, 'index.html', {'mensaje':username})
        else:
            return render(request, "usuarios/crear.html", {"formulario":form})    
    else:
        form = form_crear_usuario()
        return render(request, 'usuarios/crear.html', {'formulario': form})


def listar_usuarios(request):
    usuarios = User.objects.all()
    return render(request, "usuarios/listar.html", {"usuarios":usuarios})



def editar_usuarios(request,id):
    usuario = User.objects.get(id=id)
    if request.method == 'POST':
        form = form_editar_usuarios(request.POST,instance=usuario)
        if form.is_valid():
            usuario.username   = form.cleaned_data.get('username')
            usuario.first_name = form.cleaned_data.get('first_name')
            usuario.last_name  = form.cleaned_data.get('last_name')
            usuario.email      = form.cleaned_data.get('email')
            usuario.save()
            return render(request, 'usuarios/editar.html', {'mensaje':"Editado correctamente"})
        else:
            return render(request, "usuarios/editar.html", {"formulario":form, "usuario":usuario, "mensaje":"FORMULARIO INVALIDO"})
    else:
        form = form_editar_usuarios(instance=usuario)
        return render(request, 'usuarios/editar.html', {'formulario': form, "usuario":usuario})
    

def eliminar_usuario(request,id):
    usuario = User.objects.get(id=id)
    usuario.delete()
    return redirect('listar_usuarios')

@login_required
def ver_perfil(request, username= None):
    current_user = request.user
    if username and username != current_user.username:
        user = User.objects.get(username=username)
    else:
        user = current_user
        return render (request, "usuarios/perfil.html", {"user":user})



#=================== USUARIOS ===============================================================================            
#============================================================================================================




#=================== EVENTOS ===============================================================================

def evento(request):
    if request.method=="POST":
        form=EventoForm(request.POST, request.FILES)
        if form.is_valid():
            informacion=form.cleaned_data
            propietario=informacion['propietario']
            titulo=informacion['titulo']
            subtitulo=informacion['subtitulo']
            cuerpo=informacion['cuerpo']
            autor=informacion['autor']
            fecha=informacion['fecha']
            imagen=informacion['imagen']
            evento=Evento_db(propietario=propietario, titulo=titulo, subtitulo=subtitulo, cuerpo=cuerpo, autor=autor, fecha=fecha, imagen=imagen)
            evento.save()
            return render(request, "eventoFormulario.html",{"mensaje":"Evento creado correctamente"})
        else:
            return render(request, "eventoFormulario.html",{"mensaje":"Formulario invalido"})
    else:
        form=EventoForm()
        return render(request, "eventoFormulario.html", {"formulario_evento":form})

def leerEventos(request):
    eventos=Evento_db.objects.all()
    return render(request, "leerEventos.html", {"eventos": eventos})

def eliminarEvento(request, id):
    evento=Evento_db.objects.get(id=id)
    evento.delete()
    eventos=Evento_db.objects.all()
    return render(request, "leerEventos.html", {"eventos": eventos})

def editarEvento(request, id):
    evento=Evento_db.objects.get(id=id)
    if request.method=="POST":
        form=EventoForm(request.POST, request.FILE)
        if form.is_valid():
            info=form.cleaned_data
            evento.propietario=info["propietario"]
            evento.titulo=info["titulo"]
            evento.subtitulo=info["subtitulo"]
            evento.cuerpo=info["cuerpo"]
            evento.autor=info["autor"]
            evento.fecha=info["fecha"]
            evento.imagen=info["imagen"]
            evento.save()
            eventos=Evento_db.objects.all()
            return render(request, "leerEventos.html", {"eventos":eventos})
        else:
            form=EventoForm(initial={"propietario":evento.propietario, "titulo":evento.titulo, "subtitulo":evento.subtitulo, "cuerpo":evento.cuerpo, "autor":evento.autor, "fecha":evento.fecha, "imagen":evento.imagen})
            return render(request, "editarEvento.html", {"formulario":form, "evento":evento})
    else:
        form=EventoForm()
        return render(request, "eventoFormulario.html", {"formulario":form})


def leerMas(request, id):
    evento=Evento_db.objects.get(id=id)
    return render(request, "leerMas.html", {"evento":evento})

def about(request):
    return render(request, "about.html")
