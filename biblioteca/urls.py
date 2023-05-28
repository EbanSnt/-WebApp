from django.urls import path
from .views import *

#REMOVER EL # PARA DEJAR FUNCIONAL EL PATH A LA URL mostrada 

urlpatterns = [
    path("",index,name="index"), 
    path("empleados/",empleado_lista, name="empleado_lista"), 
    path("empleados/nuevo/",registrar_empleado, name="registrar_empleado"),
    path("empleados/<int:id>/modificar/",actualizar_empleado, name="actualizar_empleado"),
    path("socios/", socio_lista, name="socio_lista"),
    path("socios/<int:id>/modificar/", actualizar_socio, name="actualizar_socio"),
    #path("autores/<int:id>/modificar/",modificar_autor,name="modificar_autor"),
    #path("autores/nuevo/",registrar_autor,name="registrar_autor"),
    #path("autores/",autores_lista, name="autores_lista"),
    path("autores/<int:id>/activar,",activo_cambiar_autor,name="autor_lista"),
    #path("autores/<int:id>/desactivar,",desactivar_autor,name="desactivar_autor")
    path("autores", registrar_autor, name="registrar_autor"),
]
