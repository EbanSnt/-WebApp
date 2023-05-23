from django.urls import path
from .views import *

#REMOVER EL # PARA DEJAR FUNCIONAL EL PATH ALA URL mostrada 

urlpatterns = [
    path("",index,name="index"), 
    path("empleados/",empleado_lista, name="empleado_lista"), 
    path("empleados/nuevo/",registrar_empleado, name="registrar_empleado"),
    path("empleados/<int:id>/modificar/",actualizar_empleado, name="actualizar_empleado"),
    #path("socios", socio_lista, name="socio_lista"),
]
