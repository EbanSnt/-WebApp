from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

from exportcsv.models import HistorialForm
from .forms import *
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.http import HttpResponseRedirect, JsonResponse
from datetime import timedelta
import time
from datetime import datetime
import csv
from django.http import HttpResponse

# Create your views here.
# HEADER PRESENTE EN TODAS LAS PAGINAS


def index(request):
    """
    Genera la pagina principal de la aplicacion

    Args:
        request (GET): Objeto que contiene la informacion de la solicitud HTTP

    Returns:
        POST: Redirecciona a la pagina principal
    """
    return render(request, "index.html")


# RENDER PARA UN TEMPLATE DE ERROR
# FALTA IMPLEMENTAR EN vistas!
def error(request):
    """ 
    Render de una pagina de error, la cual es mostrada cuando se produce un error 
    """
    return render(request, "error.html")  # se agrego la URL


# EMPLEADOS
def empleado_lista(request):
    """
     Genera una lista de los empleados registrados en el sitema, los cuales pueden ser editados o eliminados
     la lista generada es obtenida de forma dinamica de la base de datos y se actualiza cada vez que se accede a la pagina, 
     sin un orden especifico

    Args:
        request (GET): recibe la solicitud HTTP con toda la lsita de empleados completa

    Returns:
        POST: vuelca los datos en la base de datos 
    """
    try:
        empleados = Empleado.objects.all()
        context = {"empleados": empleados}
        return render(request, "empleado_lista.html", context)
    except Exception:
        return render(request, "empleado_lista.html")


# Crea un nuevo empleado y lo guarda en la base de datos
@csrf_exempt
def registrar_empleado(request):
    """
    Permite registrar un nuevo empleado en el sistema, el cual es almacenado en la base de datos
    """
    now = datetime.now()
    fecha = now.strftime('%d/%m/%Y %H:%M')
    form = EmpleadoForm()
    context = {'form': form, "mensaje": ""}
    if request.method == "POST":
        nombre = request.POST["nombre"]
        apellido = request.POST["apellido"]
        legajo = request.POST["numero_legajo"]
        descripcion = f"Se añade un Empleado:\n{nombre} {apellido}\n N° de Legajo: {legajo}"
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            nlegajo = form.cleaned_data["numero_legajo"]
            if (Empleado.objects.filter(numero_legajo=nlegajo).exists()):
                context["mensaje"] = "Nº de Legajo ya existe en la base de datos"
                return render(request, "empleado_nuevo.html", context)
            form.save()
            # añadido redireccion al listado para cargar el nuevo
            HistorialForm.objects.create(
                fecha=fecha, descripcion=descripcion, tipo="Creacion")
            print(datetime.now())
            return redirect("empleado_lista")
        else:
            return redirect("empleado_lista")

    return render(request, "empleado_nuevo.html", context)


@csrf_exempt
def actualizar_empleado(request, id):
    """
    Permite actualizar los datos de un empleado en especifico, los datos son obtenidos de la base de datos y cargados en los formularios
    """
    now = datetime.now()
    fecha = now.strftime('%d/%m/%Y %H:%M')
    empleado = Empleado.objects.get(id=id)
    empleado_viejo = Empleado.objects.get(id=id)
    if request.method == "POST":
        empleado.nombre = request.POST["nombre"]
        empleado.apellido = request.POST["apellido"]
        empleado.numero_legajo = request.POST["nlegajo"]
        if request.POST.get("activo") == None:
            empleado.activo = False
            activo_nuevo = "Inactivo"
        else:
            empleado.activo = True
            activo_nuevo = "Activo"

        if empleado_viejo.activo:
            activo = "Activo"
        else:
            activo = "Inactivo"
        empleado.save()

        descripcion = f"Se Actualiza un Empleado: {empleado_viejo.nombre} {empleado_viejo.apellido}. \n N° de Legajo: {empleado_viejo.numero_legajo}. Estado: {activo} --> \n{empleado.nombre} {empleado.apellido}.\n N° de Legajo: {empleado.numero_legajo}. Estado: {activo_nuevo}"
        HistorialForm.objects.create(
            fecha=fecha, descripcion=descripcion, tipo="Actualizacion")
        return redirect("empleado_lista")
    else:
        return render(request, "empleado_actualizar.html", {"empleado": empleado})


def desactivar_empleado(request, id):
    """
        Desactiva un empleado en especifico, el cual es seleccionado por el usuario, el empleado es desactivado y no puede ser utilizado en el sistema
    """
    empleado = Empleado.objects.get(id=id)
    if request.method == "POST":
        empleado.activo = False
        empleado.save()
        # Donde se usa la variable messages?
        messages.success(
            request, "El empleado ha sido desactivado exitosamente.")
        return redirect("empleado_lista")
    else:
        return render(request, "empleado_actualizar.html", {"empleado": empleado})


# ACTIVAR_DESACTIVAR UN REGISTRO DE EMPLEADO / FUSION DE CODIGO
def activo_cambiar_empleado(request, id):
    now = datetime.now()
    fecha = now.strftime('%d/%m/%Y %H:%M')
    empleado = Empleado.objects.get(id=id)
    if request.method == "POST":
        if empleado.activo == False:
            empleado.activo = True
            activo = "Activa"
            tipo = "Activacion"
        else:
            empleado.activo = False
            activo = "Desactiva"
            tipo = "Desactivacion"
        empleado.save()
        descripcion = f"Se {activo} un Empleado:\n{empleado.nombre} {empleado.apellido}\n N° de Legajo: {empleado.numero_legajo}"
        HistorialForm.objects.create(
            fecha=fecha, descripcion=descripcion, tipo=tipo)
        # REEMPLAZAR POR EL NAME DEL PATH QUE SE COLOCARÁ
        return redirect("empleado_lista")
    # REEMPLAZAR POR EL NAME DEL PATH QUE SE COLOCARÁ
    return render(request, "status_empleado")


@csrf_exempt
def borrar_empleado(request, id):
    empleado = get_object_or_404(Empleado, id=id)
    e  = Empleado.objects.get(id=id)
    socios = Socio.objects.all()
    libros = Libro.objects.all()
    prestamos = Prestamo_libro.objects.all()
    empleados = Empleado.objects.all()
    now = datetime.now()
    fecha = now.strftime('%d/%m/%Y %H:%M')
    if request.method == "POST":
        descripcion = f"Se Elimina un Empleado:\n{empleado.nombre} {empleado.apellido}\n N° de Legajo: {empleado.numero_legajo}"
        empleado.delete()
        HistorialForm.objects.create(
            fecha=fecha, descripcion=descripcion, tipo="Eliminacion")
        return redirect("empleado_lista")

    return render(request, "empleado_borrar.html", {"empleado": empleado,"socios":socios,"libros":libros,"prestamos":prestamos,"empleados":empleados,"e":e})


# AUTORES
def autor_lista(request):
    """
    Genera una lista de los autores registrados en el sitema, los cuales pueden ser editados o eliminados
    """
    try:
        autores = Autor.objects.all()
        context = {"autores": autores}
        return render(request, "autor_lista.html", context)
    except Exception:
        return render(request, "autor_lista.html")


def desactvar_autor(request, id):
    """
    Desactiva un autor en especifico, el cual es seleccionado por el usuario, el autor es desactivado y no puede ser utilizado en el sistema
    """
    autor = Autor.objects.get(id=id)
    if request.method == "POST":
        autor.activo = False
        autor.save()
        messages.success(request, "El Autor ha sido desactivado exitosamente")
        return redirect("autor_lista")
    else:
        return render(request, "autor_actulizar.html", {"autor": autor})


@csrf_exempt
def registrar_autor(request):
    """
     Registro de autores en el sistema, los cuales son almacenados en la base de datos, los parametros son obtenidos de los formularios 
    """
    now = datetime.now()
    fecha = now.strftime('%d/%m/%Y %H:%M')
    form = AutoresForm()  # REEMPLAZAR POR EL FORM PARA ESTE CAMPO
    if request.method == "POST":
        form = AutoresForm(request.POST)
        if form.is_valid():
            form.save()
            nombre = request.POST["nombre"]
            apellido = request.POST["apellido"]
            nacionalidad = request.POST["nacionalidad"]
            descripcion = f"Se añade un Autor:\n{nombre} {apellido}\n ({nacionalidad})"
            HistorialForm.objects.create(
                fecha=fecha, descripcion=descripcion, tipo="Creacion")
            return redirect("autor_lista")
        else:
            # REEMPLAZAR POR EL TEMPLATE PARA ESTE CAMPO
            return redirect("autor_lista.html")
    context = {"form": form}
    # REEMPLAZAR POR EL TEMPLATE QUE SE CREARÁ
    return render(request, "autores_nuevo.html", context)


@csrf_exempt
# ACTUALIZAR REGISTRO DE UN AUTOR
def actualizar_autor(request, id):
    """
        Actualiza los datos de un autor en especifico, los datos son obtenidos de la base de datos y cargados en los formularios para que el usuario pueda modificarlosa gusto siempre y cuando cumplan con las validaciones
    """
    now = datetime.now()
    fecha = now.strftime('%d/%m/%Y %H:%M')
    autor = Autor.objects.get(id=id)
    autor_viejo = Autor.objects.get(id=id)
    if request.method == "POST":
        autor.nombre = request.POST["nombre"]
        autor.apellido = request.POST["apellido"]
        autor.nacionalidad = request.POST["nacionalidad"]
        if request.POST.get("activo") == None:
            autor.activo = False
            activo = "Inactivo"
        else:
            autor.activo = True
            activo = "Activo"

        if autor_viejo.activo:
            activo_viejo = "Activo"
        else:
            activo_viejo = "Inactivo"
        descripcion = f"Se Actualiza un Autor:\n{autor_viejo.nombre} {autor_viejo.apellido}\n ({autor_viejo.nacionalidad}). Estado: {activo_viejo} --> \n {autor.nombre} {autor.apellido}\n ({autor.nacionalidad}). Estado: {activo}"
        autor.save()

        HistorialForm.objects.create(
            fecha=fecha, descripcion=descripcion, tipo="Actualizacion")

        return redirect("autor_lista")
    else:
        return render(request, "autores_actualizar.html", {"autor": autor})


# ACTIVAR UN REGISTRO DE AUTOR
def activo_cambiar_autor(request, id):
    """
        Activa un autor en especifico, el cual es seleccionado por el usuario, el autor es activado y puede ser utilizado en el sistema
    """
    now = datetime.now()
    fecha = now.strftime('%d/%m/%Y %H:%M')
    autor = Autor.objects.get(id=id)
    if request.method == "POST":
        if autor.activo == False:
            autor.activo = True
            activo = "Activa"
            tipo = "Activacion"
        else:
            autor.activo = False
            activo = "Desactiva"
            tipo = "Desactivacion"
        descripcion = f"Se {activo} un Autor:\n{autor.nombre} {autor.apellido}\n ({autor.nacionalidad})"
        autor.save()

        HistorialForm.objects.create(
            fecha=fecha, descripcion=descripcion, tipo=tipo)
        # REEMPLAZAR POR EL NAME DEL PATH QUE SE COLOCARÁ
        return redirect("autor_lista")
    # REEMPLAZAR POR EL NAME DEL PATH QUE SE COLOCARÁ
    return render(request, "status_autor")


@csrf_exempt
def borrar_autor(request, id):
    autor = get_object_or_404(Autor, id=id)
    libros = Libro.objects.all()
    prestamos = Prestamo_libro.objects.all()
    empleados = Empleado.objects.all()
    socios = Socio.objects.all()
    now = datetime.now()
    fecha = now.strftime('%d/%m/%Y %H:%M')
    if request.method == "POST":
        descripcion = f"Se Elimina un Autor:\n{autor.nombre} {autor.apellido}\n ({autor.nacionalidad})"
        autor.delete()
        HistorialForm.objects.create(
            fecha=fecha, descripcion=descripcion, tipo="Eliminacion")
        return redirect("autor_lista")

    return render(request, "autor_borrar.html", {"autor": autor,"libros":libros,"prestamos":prestamos,"socios":socios,"empleados":empleados})


# SOCIOS
# Rgristrar un socio
@csrf_exempt
def registrar_socio(request) -> HttpResponseRedirect:
    """
        Registro de socios en el sistema, los cuales son almacenados en la base de datos, los parametros son obtenidos de los formularios
    """
    now = datetime.now()
    fecha = now.strftime('%d/%m/%Y %H:%M')
    form = SociosForm()  # REEMPLAZAR POR EL FORM PARA ESTE CAMPO
    if request.method == "POST":
        form = SociosForm(request.POST)
        if form.is_valid():
            form.save()
            nombre = request.POST["nombre"]
            apellido = request.POST["apellido"]
            descripcion = f"Se Añade un Socio:\n{nombre} {apellido}\n"
            HistorialForm.objects.create(
                fecha=fecha, descripcion=descripcion, tipo="Creacion")
            return redirect("socio_lista")
    context = {"form": form}
    # REEMPLAZAR POR EL TEMPLATE QUE SE CREARÁ
    return render(request, "socio_nuevo.html", context)

# LIST DE SOCIOS


def socio_lista(request):
    """
        Lista de socios registrados en el sistema, los cuales pueden ser editados o eliminados, esta es obtenida desde la base de datos
    """
    try:
        socios = Socio.objects.all()
        context = {"socios": socios}
        return render(request, "socio_lista.html", context)
    except Exception:
        return render(request, "socio_lista.html")


@csrf_exempt
# ACTUALIZAR REGISTRO DE UN SOCIO
def actualizar_socio(request, id):
    """
        Actualiza los datos de un socio en especifico, los datos son obtenidos de la base de datos y cargados en los formularios para que el usuario pueda modificarlosa gusto siempre y cuando cumplan con las validaciones
    """
    now = datetime.now()
    fecha = now.strftime('%d/%m/%Y %H:%M')
    socio = Socio.objects.get(id=id)
    socio_viejo = Socio.objects.get(id=id)
    if request.method == "POST":
        socio.nombre = request.POST["nombre"]
        socio.apellido = request.POST["apellido"]
        socio.fecha_nacimiento = request.POST["fnacimiento"]
        if request.POST.get("activo") == None:
            socio.activo = False
            activo = "Inactivo"
        else:
            socio.activo = True
            activo = "Activo"

        if socio_viejo.activo:
            activo_viejo = "Activo"
        else:
            activo_viejo = "Inactivo"

        socio.save()
        descripcion = f"Se Actualiza un Socio:\n{socio_viejo.nombre} {socio_viejo.apellido}. Estado: {activo_viejo}\n -->\n {socio.nombre} {socio.apellido}. Estado: {activo}"
        HistorialForm.objects.create(
            fecha=fecha, descripcion=descripcion, tipo="Actualizacion")
        return redirect("socio_lista")
    else:
        return render(request, "socio_actualizar.html", {"socio": socio})


# Desactivar un socio
def desactivar_socio(request, id):
    """
        Desactiva un socio en especifico, el cual es seleccionado por el usuario, el socio es desactivado y no puede ser utilizado en el sistema
    """
    socio = Socio.objects.get(id=id)
    if request.method == "POST":
        socio.activo = False
        socio.save()
        messages.success(request, "El Socio ha sido desactivado exitosamente.")
        return redirect("socio_lista")
    else:
        return render(request, "socio_lista.html", {"socio": socio})

# Activar un socio


def activar_socio(request, id):
    socio = Socio.objects.get(id=id)
    if request.method == "POST":
        socio.activo = True
        socio.save()
        messages.success(request, "El Socio ha sido activado exitosamente.")
        return redirect("socio_lista")
    else:
        return render(request, "socio_lista.html", {"socio": socio})

# FUSION DE CODIGO


def activar_cambiar_socio(request, id):
    now = datetime.now()
    fecha = now.strftime('%d/%m/%Y %H:%M')
    socio = Socio.objects.get(id=id)
    if request.method == "POST":
        if socio.activo == False:
            socio.activo = True
            activo = "Activa"
            tipo = "Activacion"
        else:
            socio.activo = False
            activo = "Desactiva"
            tipo = "Desactivacion"
        socio.save()
        descripcion = f"Se {activo} un Socio:\n{socio.nombre} {socio.apellido}"
        HistorialForm.objects.create(
            fecha=fecha, descripcion=descripcion, tipo=tipo)
        return redirect("socio_lista")
        # REEMPLAZAR POR EL NAME DEL PATH QUE SE COLOCARÁ
        return redirect("socio_lista")
    # REEMPLAZAR POR EL NAME DEL PATH QUE SE COLOCARÁ
    return render(request, "status_socio")


@csrf_exempt
def borrar_socio(request, id):
    socio = get_object_or_404(Socio, id=id)
    empleados = Empleado.objects.all()
    prestamos = Prestamo_libro.objects.all()
    libros = Libro.objects.all()
    now = datetime.now()
    fecha = now.strftime('%d/%m/%Y %H:%M')
    if request.method == "POST":
        descripcion = f"Se Elimina un Socio:\n{socio.nombre} {socio.apellido}"
        socio.delete()
        HistorialForm.objects.create(
            fecha=fecha, descripcion=descripcion, tipo="Eliminacion")
        return redirect("socio_lista")

    return render(request, "socio_borrar.html", {"socio": socio,"empleados":empleados,"libros":libros,"prestamos":prestamos})


"""
    VIEWS LIBROS
    BEGINS HERE
"""
# MOSTRAR LA LISTA DE LIBROS


def libro_lista(request):
    """ 
        Lista de libros registrados en el sistema, los cuales pueden ser editados o eliminados, esta es obtenida desde la base de datos
    """
    try:
        libros = Libro.objects.all()
        context = {"libros": libros}
        # REEMPLAZAR POR EL NAME DEL TEMPLATE
        return render(request, "libro_lista.html", context)
    except Exception:
        return render(request, "libro_lista.html")


# Registrar un libro
@csrf_exempt
def registrar_libro(request) -> HttpResponseRedirect:
    """
        Registro de libros en el sistema, los cuales son almacenados en la base de datos, los parametros son obtenidos de los formularios
    """
    now = datetime.now()
    fecha = now.strftime('%d/%m/%Y %H:%M')
    form = LibroForm()  # REEMPLAZAR POR EL FORM PARA ESTE CAMPO
    if request.method == "POST":
        form = LibroForm(request.POST)
        if form.is_valid():
            titulo = request.POST["titulo"]
            isbn = request.POST["isbn"]
            autor = Autor.objects.get(id=request.POST["autor"])
            if (Libro.objects.filter(isbn=isbn).exists()):
                return render(request, "libro_nuevo.html", {"form": form, "mensaje": "Un libro con este isbn ya existe"})
            form.save()
            descripcion = f"Se Añade un Libro:\n{titulo}\n({autor.nombre} {autor.apellido})\nISBN: {isbn}"
            HistorialForm.objects.create(
                fecha=fecha, descripcion=descripcion, tipo="Creacion")
            return redirect("libros_lista")
    context = {"form": form}
    # REEMPLAZAR POR EL TEMPLATE QUE SE CREARÁ
    return render(request, "libro_nuevo.html", context)


@csrf_exempt
# ACTUALIZAR REGISTRO DE UN LIBRO
def actualizar_libro(request, id):
    """
        Actualiza los datos de un libro en especifico, los datos son obtenidos de la base de datos y cargados en los formularios para que el usuario pueda modificarlosa gusto siempre y cuando cumplan con las validaciones
    """
    now = datetime.now()
    fecha = now.strftime('%d/%m/%Y %H:%M')
    libro = Libro.objects.get(id=id)
    libro_viejo = Libro.objects.get(id=id)
    autor_libro_actual = Autor.objects.get(id=libro.autor.id)
    autor = Autor.objects.filter(~Q(nombre=libro.autor))
    if request.method == "POST":
        libro.titulo = request.POST["titulo"]
        libro.descripcion = request.POST["descripcion"]
        libro.isbn = request.POST["isbn"]
        autor_id = Autor.objects.get(id=int(request.POST["autor"]))
        libro.autor = autor_id
        libro.activo = request.POST.get('activo', None)
        if request.POST.get("activo") == None:
            libro.activo = False
            activo = "Inactivo"
        else:
            libro.activo = True
            activo = "Activo"

        if libro_viejo.activo:
            activo_viejo = "Activo"
        else:
            activo_viejo = "Inactivo"

        libro.save()
        descripcion = f"Se Actualiza un Libro:\n{libro_viejo.titulo}\n({libro_viejo.autor.nombre} {libro_viejo.autor.apellido})\nISBN: {libro_viejo.isbn}. Estado: {activo_viejo} -->\n{libro.titulo}\n({libro.autor.nombre} {libro.autor.apellido})\nISBN: {libro.isbn}. Estado: {activo}"
        HistorialForm.objects.create(
            fecha=fecha, descripcion=descripcion, tipo="Actualizacion")
        # REEMPLAZAR AQUI CON EL NAME DE LA RUTA EN URLS.PY
        return redirect("libros_lista")
    else:
        # REEMPLAZAR CON EL NOMBRE DEL TEMPLATE QUE SE USARÁ
        return render(request, "libro_actualizar.html", {"libro": libro, "autores": autor, "autor_actual": autor_libro_actual})

# FUSION DE CODIGO


def activar_cambiar_libro(request, id):
    """
        Desactiva un libro en especifico, el cual es seleccionado por el usuario, el libro es desactivado y no puede ser utilizado en el sistema
    """
    now = datetime.now()
    fecha = now.strftime('%d/%m/%Y %H:%M')
    libro = Libro.objects.get(id=id)
    if request.method == "POST":
        if libro.activo == False:
            libro.activo = True
            activo = "Activa"
            tipo = "Activacion"
        else:
            libro.activo = False
            activo = "Desactiva"
            tipo = "Desactivacion"
        libro.save()
        descripcion = f"Se {activo} un Libro:\n{libro.titulo}\n({libro.autor.nombre} {libro.autor.apellido})\nISBN: {libro.isbn}"
        HistorialForm.objects.create(
            fecha=fecha, descripcion=descripcion, tipo=tipo)
        return redirect("libros_lista")
    return render(request, "status_libros")


@csrf_exempt
def borrar_libro(request, id):
    libro = get_object_or_404(Libro, id=id)
    autor_libro_actual = Autor.objects.get(id=libro.autor.id)
    socios = Socio.objects.all()
    prestamos = Prestamo_libro.objects.all()
    empleados = Empleado.objects.all()
    libros = Libro.objects.all()
    now = datetime.now()
    fecha = now.strftime('%d/%m/%Y %H:%M')
    if request.method == "POST":
        libro.delete()
        descripcion = f"Se Elimina un Libro:\n{libro.titulo}\n({libro.autor.nombre} {libro.autor.apellido})\nISBN: {libro.isbn}"
        HistorialForm.objects.create(
            fecha=fecha, descripcion=descripcion, tipo="Eliminacion")
        return redirect("libros_lista")

    return render(request, "libro_borrar.html", {"libro": libro, "autor_actual": autor_libro_actual,"socios":socios,"empleados":empleados,"prestamos":prestamos,"libros":libros})


"""
    VIEWS PRESTAMOS
    BEGINS HERE
"""


def prestamos_lista(request):
    """
        Lista de prestamos registrados en el sistema, los cuales pueden ser editados o eliminados, esta es obtenida desde la base de datos
    """
    prestamos = Prestamo_libro.objects.all()
    context = {"prestamos": prestamos}
    try:
        return render(request, "prestamos_lista.html", context)
    except:
        return render(request, "prestamos_lista.html")


def PrestarForm(request):
    """
        Formulario para prestar un libro, el cual es obtenido desde la base de datos y cargado en el formulario para que el usuario pueda seleccionar el libro que desea prestar
        esta view regula las validaciones
    """
    now = datetime.now()
    fecha = now.strftime('%d/%m/%Y %H:%M')
    form = PrestamoLibroForm()
    if request.method == "POST":
        form = PrestamoLibroForm(request.POST)
        if form.is_valid():
            # PARA QUE NO GUARDE AL DAR AL BOTON DE ENVIAR
            prestamo = form.save(commit=False)

            # CALCULOS PARA LA FECHA DE DEVOLUCION DEL LIBRO
            fecha_prestamo = prestamo.fecha_prestamo
            prestamo.fecha_devolucion = fecha_prestamo + timedelta(days=2)

            socio = Socio.objects.get(id=request.POST['socio'])
            libro = Libro.objects.get(id=request.POST['libro'])
            empleado = Empleado.objects.get(id=request.POST['empleado'])
            fecha_prestamo = request.POST['fecha_prestamo']

            prestamo.save()  # GUARDAMOS RECIEN AQUI EL REGISTRO
            descripcion = f"Se Añade un Prestamo:\n'{libro.titulo}'para {socio.nombre} {socio.apellido}.\nPrestamo hecho por: {empleado.nombre} {empleado.apellido} (Legajo:{empleado.numero_legajo})\nDia: {fecha_prestamo}"
            HistorialForm.objects.create(
                fecha=fecha, descripcion=descripcion, tipo="Creacion")
            return redirect('prestamos_lista')
    else:
        form = PrestamoLibroForm()

    context = {'form': form}
    return render(request, 'prestamo_libro.html', context)


@csrf_exempt
# ACTUALIZAR UN PRESTAMO
def actualizar_prestamo(request, id):
    """
        Actualiza los datos de un prestamo en especifico, los datos son obtenidos de la base de datos y cargados en los formularios para que el usuario pueda modificarlos a gusto siempre y cuando cumplan con las validaciones
    """
    now = datetime.now()
    fecha = now.strftime('%d/%m/%Y %H:%M')
    prestamo = Prestamo_libro.objects.get(id=id)
    prestamo_viejo = Prestamo_libro.objects.get(id=id)
    socio_actual = Socio.objects.get(id=prestamo.socio.id)
    empleado_actual = Empleado.objects.get(id=prestamo.empleado.id)
    libro_actual = Libro.objects.get(id=prestamo.libro.id)
    socio = Socio.objects.filter(~Q(id=prestamo.socio.id))
    empleado = Empleado.objects.filter(~Q(id=prestamo.empleado.id))
    libro = Libro.objects.filter(~Q(id=prestamo.libro.id))
    if request.method == "POST":
        socio_id = Socio.objects.get(id=int(request.POST["socio"]))
        prestamo.socio = socio_id
        empleado_id = Empleado.objects.get(id=int(request.POST["empleado"]))
        prestamo.empleado = empleado_id
        libro_id = Libro.objects.get(id=int(request.POST["libro"]))
        prestamo.libro = libro_id
        prestamo.fecha_prestamo = request.POST["fecha_prestamo"]
        prestamo.fecha_devolucion = request.POST["fecha_devolucion"]
        prestamo.save()
        descripcion = f"Se Actualiza un Prestamo:\n'{prestamo_viejo.libro.titulo}' para {prestamo_viejo.socio.nombre} {prestamo_viejo.socio.apellido}.\nPrestamo hecho por: {prestamo_viejo.empleado.nombre} {prestamo_viejo.empleado.apellido} (Legajo:{prestamo_viejo.empleado.numero_legajo})\nDia: {prestamo_viejo.fecha_prestamo} --> \n {prestamo.libro.titulo}' para {prestamo.socio.nombre} {prestamo.socio.apellido}.\nPrestamo hecho por: {prestamo.empleado.nombre} {prestamo.empleado.apellido} (Legajo:{prestamo.empleado.numero_legajo})\nDia: {prestamo.fecha_prestamo}"
        HistorialForm.objects.create(
            fecha=fecha, descripcion=descripcion, tipo="Actualizacion")
        return redirect('prestamos_lista')
    else:
        # REEMPLAZAR CON EL NOMBRE DEL TEMPLATE QUE SE USARÁ
        return render(request, "prestamo_actualizar.html", {"prestamo": prestamo, "socios": socio, "socio_actual": socio_actual, "empleados": empleado, "empleado_actual": empleado_actual, "libros": libro, "libro_actual": libro_actual})


'''def borrar_prestamo_libro(request, id):
    """
        Elimina un prestamo en especifico, el cual es seleccionado por el usuario, el prestamo es eliminado y no puede ser utilizado en el sistema
    """
    try:
        prestamo = get_object_or_404(Prestamo_libro, id=id) # en caso de no encontrar el ID retorna un 404 

        if request.method == "POST":
            prestamo.delete()
            messages.success(request, "El préstamo ha sido eliminado exitosamente.")
            return redirect("prestamos_lista") #

        return render(request, "borrar_prestamo_libro.html", {"prestamo": prestamo}) # Agregue una web para borrado exitoso 
    
    except Exception as e:
        messages.error(request, f"No se puede eliminar el préstamo: {e}") 
        return redirect("error") # se agrego la URL'''


@csrf_exempt
def borrar_prestamo_libro(request, id):
    now = datetime.now()
    fecha = now.strftime('%d/%m/%Y %H:%M')
    prestamo = get_object_or_404(Prestamo_libro, id=id)
    socio_actual = Socio.objects.get(id=prestamo.socio.id)
    empleado_actual = Empleado.objects.get(id=prestamo.empleado.id)
    libro_actual = Libro.objects.get(id=prestamo.libro.id)

    if request.method == "POST":
        descripcion = f"Se Elimina un Prestamo:\n'{prestamo.libro.titulo}' para {prestamo.socio.nombre} {prestamo.socio.apellido}.\nPrestamo hecho por: {prestamo.empleado.nombre} {prestamo.empleado.apellido} (Legajo:{prestamo.empleado.numero_legajo})\nDia: {prestamo.fecha_prestamo}"

        prestamo.delete()
        HistorialForm.objects.create(
            fecha=fecha, descripcion=descripcion, tipo="Eliminacion")
        return redirect("prestamos_lista")

    return render(request, "prestamo_borrar.html", {"prestamo": prestamo, "libro_actual": libro_actual, "socio_actual": socio_actual, "empleado_actual": empleado_actual})
