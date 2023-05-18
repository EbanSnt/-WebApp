from django.db import models

<<<<<<< HEAD
class Autor(models.Model):

    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    nacionalidad = models.CharField(max_length=30)
    activo = models.BooleanField(default=True)
=======
# Create your models here.

class Socio(models.Model):
    
    nombre = models.CharField()
    apellido = models.CharField()
    fecha_nacimiento = models.DateField()
    activo = models.BooleanField(default=True)
>>>>>>> origin/SC5S2-16
