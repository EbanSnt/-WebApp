
from django.urls import path
from .views import *

urlpatterns =[
    path("libros/", end_libros_todos, name="GetAllLibros"),
    path("libros/<int:id>", end_libros_id,name="getLibrosID"),
    path("empleados/", end_empleados, name="GetAllEmpleados"),

]