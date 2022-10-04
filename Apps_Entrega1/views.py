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
    lista=Avatar.objects.filter(user=request.user)
    if len(lista) != 0:
        avatar = lista[0].imagen.url
    else:
        avatar = ""
    return render (request, "index.html" , {"avatar":avatar})
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


@login_required
def editar_usuarios(request):
    usuario = request.user
    if request.method == 'POST':
        form = form_editar_usuarios(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            usuario.username   = info['username']
            usuario.first_name = info['nombre']
            usuario.last_name  = info['apellido']
            usuario.email      = info['email']
            usuario.save()
            return render(request, 'usuarios/editar.html', {'mensaje':"Perfil editado correctamente"})
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
    lista=Avatar.objects.filter(user=request.user)
    if len(lista) != 0:
        avatar = lista[0].imagen.url
    else:
        avatar = ""
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

