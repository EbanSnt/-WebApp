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