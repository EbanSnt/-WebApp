from django.db import models
# Create your models here.

# Create your models here.
class Autor(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    nacionalidad = models.CharField(max_length=30)
    activo = models.BooleanField(default=True)


class Empleado(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    numero_legajo = models.CharField(max_length=30)
    activo = models.BooleanField(default=True)
    

class Socio(models.Model):

    nombre = models.CharField()
    apellido = models.CharField()
    fecha_nacimiento = models.DateField()
    activo = models.BooleanField(default=True)

class Prestamo_libro(models.Model):
    socio = models.ForeignKey(Socio, on_delete=models.CASCADE)
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    fecha_prestamo = models.DateField()
    fecha_devolucion = models.DateField()
