from django.shortcuts import render
from biblioteca.models import *
from django.http import JsonResponse
# Create your views here.

"""
    VIEWS ENDPOINT
    BEGINS HERE
"""
def end_libros_todos(request):
    #TRAEMOS TODOS LOS LIBROS
    try:
        libros = Libro.objects.all().values()
        print(libros)

        #CREAMOS UNA LISTA VACIA
        libros_data =[]
        
        for libro in libros:
            #HAY QUE TENER ENCUENTA SI TRABAJAMOS CON FOREIGN KEY, DEBEMOS BUSCAR EL FK EN SU MODELO CORRESPONDIENTE

            autor = Autor.objects.get(id=libro["autor_id"])
            
            #CREAMOS UN ELEMENTO PARA AGREGARLO A LIBROS_DATA
            libro_data ={"id":libro["id"], "titulo":libro["titulo"], "autor":autor.nombre}
        
            libros_data.append(libro_data)
        
        if not libros_data:
            raise Exception("No hay libros Registrados")

        #RETORNAMO LA LISTA EN UN JSON
        return JsonResponse(libros_data,safe=False)
    except Exception as e:
        return JsonResponse({"message":str(e)})
    
    
def end_libros_id(request,id):
    try:
        #TRAEMOS EL LIBRO
        libro = Libro.objects.get(id=id)
        print(libro)
        #CREAMOS UNA LISTA VACIA
        libro_data =[]
        #HAY QUE TENER ENCUENTA SI TRABAJAMOS CON FOREIGN KEY, DEBEMOS BUSCAR EL FK EN SU MODELO CORRESPONDIENTE
        autor = Autor.objects.get(id=libro.id)
        #CREAMOS UN ELEMENTO PARA AGREGARLO A LIBRO_DATA
        libro ={"id":libro.id, "titulo":libro.titulo,"descripcion":libro.descripcion,"autor":autor.nombre}

        libro_data.append(libro)
        #RETORNAMO LA LISTA EN UN JSON
        return JsonResponse(libro_data,safe=False)
    except:
        libro_data =[]
        return JsonResponse(libro_data,safe=False)


def end_empleados(request):
    try:
        empleados = Empleado.objects.all()
        empleados_data = [] # creamos una lista vacia
        for empleado in empleados:
            empleado_data = { 
                "id":empleado.id, # agregamos el id del empleado
                "nombre":empleado.nombre, # agregamos el nombre del empleado
                "apellido":empleado.apellido, # agregamos el apellido del empleado
                "nlegajo":empleado.numero_legajo, # agregamos el numero de legajo del empleado
                "activo":empleado.activo, # agregamos el estado del empleado
                }
            empleados_data.append(empleado_data) # agregamos el empleado_data a la lista empleados_data
        if not empleados_data:
            raise Exception("No hay empleados registrados") # si no hay empleados registrados, levantamos una excepcion
        return JsonResponse(empleados_data,safe=False)  
    except Exception as e:
        return JsonResponse({"message":str(e)}) # retornamos el mensaje de la excepcion en un json