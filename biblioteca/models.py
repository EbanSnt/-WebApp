from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.


class Autor(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    nacionalidad = models.CharField(max_length=30)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre


class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    isbn = models.BigIntegerField(
        validators=[MinValueValidator(10**12), MaxValueValidator(10**13)])
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.titulo


class Empleado(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    numero_legajo = models.CharField(max_length=30)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre


class Socio(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre


class Prestamo_libro(models.Model):
    socio = models.ForeignKey(Socio, on_delete=models.CASCADE)
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    fecha_prestamo = models.DateField()
    fecha_devolucion = models.DateField()

    def __str__(self):
        return self.libro
