from django.urls import path
from .views import *

#REMOVER EL # PARA DEJAR FUNCIONAL EL PATH A LA URL mostrada 

urlpatterns = [
    path("",index,name="index"), 
    path("error/", error, name="error"),

    #EMPLEADOS
    path("empleados/",empleado_lista, name="empleado_lista"), 
    path("empleados/nuevo/",registrar_empleado, name="registrar_empleado"),
    path("empleados/<int:id>/modificar/",actualizar_empleado, name="actualizar_empleado"),
    path("empleados/<int:id>/changeStatus",activo_cambiar_empleado, name="status_empleado"), 
    #SOCIOS
    path("socios/nuevo/", registrar_socio,name="registrar_socio"),
    path("socios/", socio_lista, name="socio_lista"),
    path("socios/<int:id>/modificar/", actualizar_socio, name="actualizar_socio"),
    path("socios/<int:id>/changeStatus", activar_cambiar_socio, name="status_socio"),
    #AUTORES
    path("autores/<int:id>/modificar/", actualizar_autor,name="actualizar_autor"),
    path("autores/nuevo/",registrar_autor,name="registrar_autor"),
    path("autores/",autor_lista, name="autor_lista"),
    path("autores/<int:id>/changeStatus",activo_cambiar_autor,name="status_autor"),
    #LIBROS
    path("endpoint/libros/", end_libros_todos,name="getLibrosAll"),
    path("prestamos/eliminar/<int:id>" ,name="libro_lista"), #<- cambio arreglado de url, parte de mi tarea anterior
    
    
]
