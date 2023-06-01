
from django.urls import path
from .views import *

urlpatterns =[
    path("libros/", end_libros_todos, name="GetAllLibros")
]