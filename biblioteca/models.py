from django.db import models

# Create your models here.


class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion  = models.TextField()
    isbn = models.CharField(max_length=13, unique=True, null=False)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre