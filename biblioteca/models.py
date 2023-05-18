from django.db import models

# Create your models here.

class Autor(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    nacionalidad = models.CharField(max_length=30)
    activo = models.BooleanField(default=True)

    
class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion  = models.TextField()
    isbn = models.CharField(max_length=13, unique=True, null=False)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre