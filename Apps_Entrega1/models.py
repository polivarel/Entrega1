from django.db import models

class eventos(models.Model):
    fecha_inicio=models.CharField(max_length=10,blank=True,null=True)
    lugar       =models.CharField(max_length=50,blank=True,null=True)
    tipo        =models.CharField(max_length=30,blank=True,null=True)
    titulo      =models.CharField(max_length=50,blank=True,null=True)
    hora_inicio =models.CharField(max_length=5,blank=True,null=True)
    aforo       =models.CharField(max_length=50,blank=True,null=True)
    genero      =models.CharField(max_length=50,blank=True,null=True)
    edad_minima =models.CharField(max_length=50,blank=True,null=True)
    duracion    =models.CharField(max_length=50,blank=True,null=True)
    puntaje     =models.CharField(max_length=50,blank=True,null=True)
    elenco      =models.CharField(max_length=50,blank=True,null=True)
    sector      =models.CharField(max_length=50,blank=True,null=True)
    equipos     =models.CharField(max_length=500,blank=True,null=True)
    deporte     =models.CharField(max_length=50,blank=True,null=True)
    contacto    =models.CharField(max_length=1000,blank=True,null=True)