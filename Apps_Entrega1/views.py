from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def inicio(request):
   mymembers = {'saludo':"Hola"}#"Members.objects.all().values()"
   template = loader.get_template('index.html')
   context = {
   'mymembers': mymembers,
   }
   return HttpResponse(template.render(context, request))


def ingresar_pelicula(request):
   mymembers = {'saludo':"Hola"}#"Members.objects.all().values()"
   template = loader.get_template('agregar.html')
   context = {
   'mymembers': mymembers,
   }
   return HttpResponse(template.render(context, request))   

#def test(request):
#    nom="Pablo"
#    ape="Olivare"
#    diccionario={'nombre':nom,'apellido':ape}
#    miArchivo=open('C:/Users/poliv/OneDrive/Documentos/Python/Clase18/Clase18/Clase18/plantillas/index.html')
#    contenido=miArchivo.read()
#    miArchivo.close()
#    plantilla=Template(contenido)
#    contexto=Context(diccionario)
#    documento=plantilla.render(contexto)
#    return HttpResponse(documento)