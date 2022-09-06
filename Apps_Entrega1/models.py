from django.db import models

class peliculas(models.Model):
    fecha_inicio=models.DateField(max_length=10,blank=True,null=True)
    lugar       =models.CharField(max_length=50,blank=True,null=True)
    titulo      =models.CharField(max_length=50,blank=True,null=True)
    hora_inicio =models.TimeField(max_length=5,blank=True,null=True)
    edad_minima =models.IntegerField(max_length=50,blank=True,null=True)
    puntaje     =models.IntegerField(max_length=50,blank=True,null=True)
    
class teatro(models.Model):
    fecha_inicio=models.DateField(max_length=10,blank=True,null=True)
    lugar       =models.CharField(max_length=50,blank=True,null=True)
    titulo      =models.CharField(max_length=50,blank=True,null=True)
    hora_inicio =models.TimeField(max_length=5,blank=True,null=True)
    elenco     =models.CharField(max_length=1000,blank=True,null=True)

class deporte(models.Model):
    fecha_inicio=models.DateField(max_length=10,blank=True,null=True)
    lugar       =models.CharField(max_length=50,blank=True,null=True)
    titulo      =models.CharField(max_length=50,blank=True,null=True)
    hora_inicio =models.TimeField(max_length=5,blank=True,null=True)
    equipo1     =models.CharField(max_length=100,blank=True,null=True)
    equipo2     =models.CharField(max_length=100,blank=True,null=True)
    deporte     =models.CharField(max_length=100,blank=True,null=True)