from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from .forms import *
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.http import HttpResponseRedirect, JsonResponse
from datetime import timedelta


# Create your views here.
#HEADER PRESENTE EN TODAS LAS PAGINAS
def index(request):
    """
    Genera la pagina principal de la aplicacion

    Args:
        request (GET): Objeto que contiene la informacion de la solicitud HTTP

    Returns:
        POST: Redirecciona a la pagina principal
    """
    return render(request,"index.html")


# RENDER PARA UN TEMPLATE DE ERROR
#FALTA IMPLEMENTAR EN vistas!
def error(request):
    """ 
    Render de una pagina de error, la cual es mostrada cuando se produce un error 
    """
    return render(request, "error.html") # se agrego la URL


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
        context = {"empleados": empleados }
        return render(request, "empleado_lista.html", context)
    except Exception:
         return render(request, "empleado_lista.html")


#Crea un nuevo empleado y lo guarda en la base de datos
@csrf_exempt
def registrar_empleado(request):
    """
    Permite registrar un nuevo empleado en el sistema, el cual es almacenado en la base de datos
    """
    form = EmpleadoForm()
    context = {'form': form, "mensaje":""}
    if request.method == "POST":
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            nlegajo = form.cleaned_data["numero_legajo"]
            if(Empleado.objects.filter(numero_legajo = nlegajo).exists()):
               context["mensaje"] = "Nº de Legajo ya existe en la base de datos"
               return render(request, "empleado_nuevo.html", context) 
            form.save()
            return redirect("empleado_lista")   # añadido redireccion al listado para cargar el nuevo 
        else:
            return redirect("empleado_lista")
  
    return render(request, "empleado_nuevo.html", context)


@csrf_exempt
def actualizar_empleado(request,id):
    """
    Permite actualizar los datos de un empleado en especifico, los datos son obtenidos de la base de datos y cargados en los formularios
    """
    empleado = Empleado.objects.get(id=id)
    if request.method =="POST": 
        print(request.POST["nlegajo"])
        empleado.nombre = request.POST["nombre"]
        empleado.apellido = request.POST["apellido"]
        empleado.numero_legajo = request.POST["nlegajo"]
        if request.POST.get("activo") == None:
            empleado.activo = False
        else:
            empleado.activo = True
        empleado.save()
        return redirect("empleado_lista")
    else:
        return render(request,"empleado_actualizar.html",{"empleado":empleado})


def desactivar_empleado(request, id):

    """
        Desactiva un empleado en especifico, el cual es seleccionado por el usuario, el empleado es desactivado y no puede ser utilizado en el sistema
    """
    empleado = Empleado.objects.get(id=id)
    if request.method == "POST":
        empleado.activo = False
        empleado.save()
        messages.success(request, "El empleado ha sido desactivado exitosamente.") # Donde se usa la variable messages?
        return redirect("empleado_lista")
    else:
        return render(request, "empleado_actualizar.html", {"empleado": empleado})


# ACTIVAR_DESACTIVAR UN REGISTRO DE EMPLEADO / FUSION DE CODIGO 
def activo_cambiar_empleado(request, id):
    empleado = Empleado.objects.get(id=id)
    if request.method == "POST":
        if empleado.activo == False:
            empleado.activo = True
        else:
            empleado.activo = False
        empleado.save()
        return redirect("empleado_lista") #REEMPLAZAR POR EL NAME DEL PATH QUE SE COLOCARÁ
    return render(request,"status_empleado") #REEMPLAZAR POR EL NAME DEL PATH QUE SE COLOCARÁ 


# AUTORES
def autor_lista(request):
    """
    Genera una lista de los autores registrados en el sitema, los cuales pueden ser editados o eliminados
    """
    try:
        autores = Autor.objects.all()
        context = {"autores": autores }
        return render(request, "autor_lista.html", context)
    except Exception:
         return render(request, "autor_lista.html")  
    

def desactvar_autor(request, id):
    """
    Desactiva un autor en especifico, el cual es seleccionado por el usuario, el autor es desactivado y no puede ser utilizado en el sistema
    """
    autor = Autor.objects.get(id = id)
    if request.method =="POST":
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
    form = AutoresForm() #REEMPLAZAR POR EL FORM PARA ESTE CAMPO
    if request.method == "POST":
        form = AutoresForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("autor_lista")
        else:
            return redirect("autor_lista.html") #REEMPLAZAR POR EL TEMPLATE PARA ESTE CAMPO
    context = {"form":form}
    return render(request, "autores_nuevo.html", context) #REEMPLAZAR POR EL TEMPLATE QUE SE CREARÁ


@csrf_exempt
# ACTUALIZAR REGISTRO DE UN AUTOR
def actualizar_autor(request,id):
    """
        Actualiza los datos de un autor en especifico, los datos son obtenidos de la base de datos y cargados en los formularios para que el usuario pueda modificarlosa gusto siempre y cuando cumplan con las validaciones
    """
    autor = Autor.objects.get(id=id)
    if request.method =="POST": 
        autor.nombre = request.POST["nombre"]
        autor.apellido = request.POST["apellido"]
        autor.nacionalidad= request.POST["nacionalidad"]
        if request.POST.get("activo") == None:
            autor.activo = False
        else:
            autor.activo = True
        autor.save()
        return redirect("autor_lista")
    else:
        return render(request,"autores_actualizar.html",{"autor":autor})
    

# ACTIVAR UN REGISTRO DE AUTOR
def activo_cambiar_autor(request, id):
    """
        Activa un autor en especifico, el cual es seleccionado por el usuario, el autor es activado y puede ser utilizado en el sistema
    """
    autor = Autor.objects.get(id=id)
    if request.method == "POST":
        if autor.activo == False:
            autor.activo = True
        else:
            autor.activo = False
        autor.save()
        return redirect("autor_lista") #REEMPLAZAR POR EL NAME DEL PATH QUE SE COLOCARÁ
    return render(request,"status_autor") #REEMPLAZAR POR EL NAME DEL PATH QUE SE COLOCARÁ 
        

# SOCIOS
# Rgristrar un socio
@csrf_exempt
def registrar_socio(request)->HttpResponseRedirect:
    """
        Registro de socios en el sistema, los cuales son almacenados en la base de datos, los parametros son obtenidos de los formularios
    """ 
    form = SociosForm() #REEMPLAZAR POR EL FORM PARA ESTE CAMPO
    if request.method == "POST":
        form = SociosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("socio_lista")
        else:
            return redirect("socio_lista.html") #REEMPLAZAR POR EL TEMPLATE PARA ESTE CAMPO
    context = {"form":form}
    return render(request, "socio_nuevo.html", context) #REEMPLAZAR POR EL TEMPLATE QUE SE CREARÁ

#LIST DE SOCIOS
def socio_lista(request):
    """
        Lista de socios registrados en el sistema, los cuales pueden ser editados o eliminados, esta es obtenida desde la base de datos
    """
    try:
        socios = Socio.objects.all()
        context = {"socios": socios }
        return render(request, "socio_lista.html", context)
    except Exception:
         return render(request, "socio_lista.html")  


@csrf_exempt
# ACTUALIZAR REGISTRO DE UN SOCIO
def actualizar_socio(request,id):
    """
        Actualiza los datos de un socio en especifico, los datos son obtenidos de la base de datos y cargados en los formularios para que el usuario pueda modificarlosa gusto siempre y cuando cumplan con las validaciones
    """
    socio = Socio.objects.get(id=id)
    if request.method =="POST": 
        socio.nombre = request.POST["nombre"]
        socio.apellido = request.POST["apellido"]
        socio.fecha_nacimiento= request.POST["fnacimiento"]
        if request.POST.get("activo") == None:
            socio.activo = False
        else:
            socio.activo = True
        socio.save()
        return redirect("socio_lista")
    else:
        return render(request,"socio_actualizar.html",{"socio":socio})
    

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

#FUSION DE CODIGO
def activar_cambiar_socio(request,id):
    socio = Socio.objects.get(id=id)
    if request.method == "POST":
        if socio.activo == False:
            socio.activo = True
        else:
            socio.activo = False
        socio.save()
        return redirect("socio_lista") #REEMPLAZAR POR EL NAME DEL PATH QUE SE COLOCARÁ
    return render(request,"status_socio") #REEMPLAZAR POR EL NAME DEL PATH QUE SE COLOCARÁ  

"""
    VIEWS LIBROS
    BEGINS HERE
"""
#MOSTRAR LA LISTA DE LIBROS
def libro_lista(request):
    """ 
        Lista de libros registrados en el sistema, los cuales pueden ser editados o eliminados, esta es obtenida desde la base de datos
    """
    try:
        libros = Libro.objects.all()
        context = {"libros": libros }
        return render(request, "libro_lista.html", context) #REEMPLAZAR POR EL NAME DEL TEMPLATE
    except Exception:
        return render(request,"libro_lista.html") 

@csrf_exempt
# ACTUALIZAR REGISTRO DE UN LIBRO
def actualizar_libro(request,id):
    """
        Actualiza los datos de un libro en especifico, los datos son obtenidos de la base de datos y cargados en los formularios para que el usuario pueda modificarlosa gusto siempre y cuando cumplan con las validaciones
    """

    libro = Libro.objects.get(id=id)
    autor_libro_actual = Autor.objects.get(nombre = libro.autor)
    autor = Autor.objects.filter(~Q(nombre=libro.autor))       
    if request.method =="POST": 
        libro.titulo = request.POST["titulo"]
        libro.descripcion = request.POST["descripcion"]
        libro.isbn = request.POST["isbn"]
        autor_id = Autor.objects.get(id = int(request.POST["autor"]))
        libro.autor = autor_id
        libro.activo= request.POST["activo"]
        if request.POST.get("activo") == None:
            libro.activo = False
        else:
            libro.activo = True
        libro.save()
        return redirect("libros_lista") #REEMPLAZAR AQUI CON EL NAME DE LA RUTA EN URLS.PY
    else:
        return render(request,"libro_actualizar.html",{"libro":libro,"autores":autor,"autor_actual":autor_libro_actual}) #REEMPLAZAR CON EL NOMBRE DEL TEMPLATE QUE SE USARÁ
    
#FUSION DE CODIGO
def activar_cambiar_libro(request,id):
    """
        Desactiva un libro en especifico, el cual es seleccionado por el usuario, el libro es desactivado y no puede ser utilizado en el sistema
    """

    libro = Libro.objects.get(id=id)
    if request.method == "POST":
        if libro.activo == False:
            libro.activo = True
        else:
            libro.activo = False
        libro.save()
        return redirect("libros_lista") 
    return render(request,"status_libros") 


"""
    VIEWS PRESTAMOS
    BEGINS HERE
"""
def prestamos_lista(request):
    """
        Lista de prestamos registrados en el sistema, los cuales pueden ser editados o eliminados, esta es obtenida desde la base de datos
    """
    prestamos = Prestamo_libro.objects.all() 
    context = {"prestamos":prestamos}
    try:
        return render(request,"prestamos_lista.html",context)
    except:
        return render(request,"prestamos_lista.html")


def PrestarForm(request):
    """
        Formulario para prestar un libro, el cual es obtenido desde la base de datos y cargado en el formulario para que el usuario pueda seleccionar el libro que desea prestar
        esta view regula las validaciones
    """
    
    form = PrestamoLibroForm()
    if request.method == "POST":
        form = PrestamoLibroForm(request.POST)
        if form.is_valid():
            prestamo = form.save(commit=False)  # PARA QUE NO GUARDE AL DAR AL BOTON DE ENVIAR

            # CALCULOS PARA LA FECHA DE DEVOLUCION DEL LIBRO
            fecha_prestamo = prestamo.fecha_prestamo
            prestamo.fecha_devolucion = fecha_prestamo + timedelta(days=2)

            prestamo.save()  # GUARDAMOS RECIEN AQUI EL REGISTRO
            return redirect('prestamos_lista')
    else:
        form = PrestamoLibroForm()

    context = {'form': form}
    return render(request, 'prestamo_libro.html', context)



def borrar_prestamo_libro(request, id):
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
        return redirect("error") # se agrego la URL
    
    
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