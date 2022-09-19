from contextlib import AbstractAsyncContextManager
from typing import AbstractSet
from django.db import models
from django.contrib.auth.models import User

class Peliculas(models.Model):
    fecha_inicio=models.DateField(blank=True,null=True)
    lugar       =models.CharField(max_length=50,blank=True,null=True)
    titulo      =models.CharField(max_length=50,blank=True,null=True)
    hora_inicio =models.TimeField(blank=True,null=True)
    edad_minima =models.IntegerField(blank=True,null=True)
    puntaje     =models.IntegerField(blank=True,null=True)

    def __str__(self):
        return self.titulo+" - "+self.lugar
    
class Teatro(models.Model):
    fecha_inicio=models.DateField(max_length=10,blank=True,null=True)
    lugar       =models.CharField(max_length=50,blank=True,null=True)
    titulo      =models.CharField(max_length=50,blank=True,null=True)
    hora_inicio =models.TimeField(max_length=5,blank=True,null=True)
    elenco     =models.CharField(max_length=1000,blank=True,null=True)

    def __str__(self):
        return self.titulo+" - "+self.lugar

class Deporte(models.Model):
    fecha_inicio=models.DateField(max_length=10,blank=True,null=True)
    lugar       =models.CharField(max_length=50,blank=True,null=True)
    titulo      =models.CharField(max_length=50,blank=True,null=True)
    hora_inicio =models.TimeField(max_length=5,blank=True,null=True)
    equipo1     =models.CharField(max_length=100,blank=True,null=True)
    equipo2     =models.CharField(max_length=100,blank=True,null=True)
    deporte     =models.CharField(max_length=100,blank=True,null=True)

    def __str__(self):
        return self.titulo+" - "+self.lugar