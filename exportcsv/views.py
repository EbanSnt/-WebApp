from django.shortcuts import render, HttpResponse
from biblioteca.models import *
import csv


from exportcsv.models import HistorialForm

# Create your views here.


def historial(request):
    historial = HistorialForm.objects.all().order_by("-fecha")
    libros = Libro.objects.all()
    autores = Autor.objects.all()
    socios = Socio.objects.all()
    empleados = Empleado.objects.all()
    prestamos = Prestamo_libro.objects.all()
    ctx = {"historial": historial, "libros": libros, "autores": autores,
           "socios": socios, "empleados": empleados, "prestamos": prestamos}
    return render(request, 'historial.html', ctx)


def autores_a_csv(request):
    # RECOGEMOS LOS DATOS
    # Obtener los registros como diccionarios
    registros = Autor.objects.all().values()

    # CREAMOS EL ARCHIVO
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="Autores.csv"'

    # PROCESO PARA ESCRIBIR
    writer = csv.writer(response)

    # Escribir encabezados de columna en el archivo CSV
    writer.writerow(registros.first().keys())

    # Escribir los registros en el archivo CSV
    for registro in registros:
        writer.writerow(registro.values())

    # RETORNO DEL CSV
    return response


def libros_a_csv(request):
    # RECOGEMOS LOS DATOS
    # Obtener los registros como diccionarios
    registros = Libro.objects.all().values()

    # CREAMOS EL ARCHIVO
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="Libro.csv"'

    # PROCESO PARA ESCRIBIR
    writer = csv.writer(response)

    # Escribir encabezados de columna en el archivo CSV
    writer.writerow(registros.first().keys())

    # Escribir los registros en el archivo CSV
    for registro in registros:
        writer.writerow(registro.values())

    # RETORNO DEL CSV
    return response


def empleado_a_csv(request):
    # RECOGEMOS LOS DATOS
    # Obtener los registros como diccionarios
    registros = Empleado.objects.all().values()

    # CREAMOS EL ARCHIVO
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="Empleados.csv"'

    # PROCESO PARA ESCRIBIR
    writer = csv.writer(response)

    # Escribir encabezados de columna en el archivo CSV
    writer.writerow(registros.first().keys())

    # Escribir los registros en el archivo CSV
    for registro in registros:
        writer.writerow(registro.values())

    # RETORNO DEL CSV
    return response


def socio_a_csv(request):
    # RECOGEMOS LOS DATOS
    # Obtener los registros como diccionarios
    registros = Socio.objects.all().values()

    # CREAMOS EL ARCHIVO
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="Socios.csv"'

    # PROCESO PARA ESCRIBIR
    writer = csv.writer(response)

    # Escribir encabezados de columna en el archivo CSV
    writer.writerow(registros.first().keys())

    # Escribir los registros en el archivo CSV
    for registro in registros:
        writer.writerow(registro.values())

    # RETORNO DEL CSV
    return response


def prestamo_a_csv(request):
    # RECOGEMOS LOS DATOS
    # Obtener los registros como diccionarios
    registros = Prestamo_libro.objects.all().values()

    # CREAMOS EL ARCHIVO
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="Prestamo_libros.csv"'

    # PROCESO PARA ESCRIBIR
    writer = csv.writer(response)

    # Escribir encabezados de columna en el archivo CSV
    writer.writerow(registros.first().keys())

    # Escribir los registros en el archivo CSV
    for registro in registros:
        writer.writerow(registro.values())

    # RETORNO DEL CSV
    return response
