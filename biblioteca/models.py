from django.db import models

# Create your models here.
class Prestamo_libro(models.Model):
    socio = models.ForeignKey(Socio, on_delete=models.CASCADE)
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    fecha_prestamo = models.DateField()
    fecha_devolucion = models.DateField()
