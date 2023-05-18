from django.db import models
# Create your models here.

class Autor(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    nacionalidad = models.CharField(max_length=30)
    activo = models.BooleanField(default=True)


class Socio(models.Model):

    nombre = models.CharField()
    apellido = models.CharField()
    fecha_nacimiento = models.DateField()
    activo = models.BooleanField(default=True)
