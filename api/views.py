from django.shortcuts import render
from biblioteca.models import *
from django.http import JsonResponse
from rest_framework import viewsets
from .serializer import *
from biblioteca.models import *



class AutorViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all().order_by('nombre')
    serializer_class = AutorSerializer

class LibroViewSet(viewsets.ModelViewSet):
    queryset = Libro.objects.all().order_by('titulo')
    serializer_class = LibroSerializer

class EmpleadoViewSet(viewsets.ModelViewSet):
    queryset = Empleado.objects.all().order_by('nombre')
    serializer_class = EmpleadoSerializer

class SocioViewSet(viewsets.ModelViewSet):
    queryset = Socio.objects.all().order_by('nombre')
    serializer_class = SocioSerializer

class Prestamo_libroViewSet(viewsets.ModelViewSet):
    queryset = Prestamo_libro.objects.all().order_by('id')
    serializer_class = Prestamo_libroSerializer

