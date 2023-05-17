from django.db import models

# Create your models here.

class Socio(models.Model):
    
    nombre = models.CharField()
    apellido = models.CharField()
    fecha_nacimiento = models.DateField()
    activo = models.BooleanField(default=True)