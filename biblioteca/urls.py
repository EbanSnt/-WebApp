from django.urls import path
from .views import *

urlpatterns = [
    path("",index,name="index"), 
    path("empleados/nuevo",registrar_empleado, name="registrar_empleado"),
]
