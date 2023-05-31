from django.shortcuts import get_object_or_404, redirect, render
from .forms import *
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.http import JsonResponse


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

    Args:
        request (GET): recibe datos de la solicitud HTTP para cargarlas en los formularios dentro del contexto

    Returns:
        _type_: retorna los datos cargados a la base de datos, la mismos datos son mostrados en la pagina especifica,
        en caso de que los datos no sean validos, se redirecciona a la pagina de registro de empleados y ser mostrados @empleado_lista
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

    Args:
        request (_type_): recibe los datos de la solicitud HTTP para cargarlos en los formularios dentro del contexto
        id (STR): id del empleado a actualizar

    Returns:
        _type_: retorna los nuevos datos la base de datos para luego ser cargados nuevamente por su respectiva funcion @empleado_lista y poder visualizarlos
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

    """_summary_

    Returns:
        _type_: _description_
    """
    empleado = Empleado.objects.get(id=id)
    if request.method == "POST":
        empleado.activo = False
        empleado.save()
        messages.success(request, "El empleado ha sido desactivado exitosamente.")
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

def autor_lista(request):
    try:
        autores = Autor.objects.all()
        context = {"autores": autores }
        return render(request, "autor_lista.html", context)
    except Exception:
         return render(request, "autor_lista.html")  
    

def desactvar_autor(request, id):
    """_summary_

    Args:
        request (_type_): _description_
        id (_type_): _description_

    Returns:
        _type_: _description_
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
def registrar_socio(request):
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


@csrf_exempt
# ACTUALIZAR REGISTRO DE UN AUTOR
def actualizar_autor(request,id):
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
    autor = Autor.objects.get(id=id)
    if request.method == "POST":
        if autor.activo == False:
            autor.activo = True
        else:
            autor.activo = False
        autor.save()
        return redirect("autor_lista") #REEMPLAZAR POR EL NAME DEL PATH QUE SE COLOCARÁ
    return render(request,"status_autor") #REEMPLAZAR POR EL NAME DEL PATH QUE SE COLOCARÁ 
        

@csrf_exempt
# ACTUALIZAR REGISTRO DE UN SOCIO
def actualizar_socio(request,id):
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
    
def socio_lista(request):
    try:
        socios = Socio.objects.all()
        context = {"socios": socios }
        return render(request, "socio_lista.html", context)
    except Exception:
         return render(request, "socio_lista.html")  



    
def desactivar_socio(request, id):
    socio = Socio.objects.get(id=id)
    if request.method == "POST":
        socio.activo = False
        socio.save()
        messages.success(request, "El Socio ha sido desactivado exitosamente.")
        return redirect("socio_lista")
    else:
        return render(request, "socio_lista.html", {"socio": socio})
    

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
    try:
        empleados = Empleado.objects.all()
        context = {"empleados": empleados }
        return render(request, "libro_lista.html", context) #REEMPLAZAR POR EL NAME DEL TEMPLATE
    except Exception:
        return render(request,"libro_lista.html") 

@csrf_exempt
# ACTUALIZAR REGISTRO DE UN LIBRO
def actualizar_libro(request,id):
    libro = Libro.objects.get(id=id)
    if request.method =="POST": 
        libro.nombre = request.POST["titulo"]
        libro.apellido = request.POST["descripcion"]
        libro.nacionalidad= request.POST["isbn"]
        libro.nacionalidad= request.POST["autor"]
        libro.nacionalidad= request.POST["activo"]
        if request.POST.get("activo") == None:
            libro.activo = False
        else:
            libro.activo = True
        libro.save()
        return redirect("libro_lista") #REEMPLAZAR AQUI CON EL NAME DE LA RUTA EN URLS.PY
    else:
        return render(request,"libro_actualizar.html",{"libro":libro}) #REEMPLAZAR CON EL NOMBRE DEL TEMPLATE QUE SE USARÁ
    

#FUSION DE CODIGO
def activar_cambiar_libro(request,id):
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
#def PrestarForm(request):
#    form = PrestamoLibroForm()
#    if request.method == "POST":
#        form = PrestamoLibroForm(request.POST)
#        if form.is_valid():
#            prestamo = form.save(commit=False)  # PARA QUE NO GUARDE AL DAR AL BOTON DE ENVIAR
#
#            # CALCULOS PARA LA FECHA DE DEVOLUCION DEL LIBRO
#            fecha_prestamo = prestamo.fecha_prestamo
#            prestamo.fecha_devolucion = fecha_prestamo + timedelta(days=2)
#
#            prestamo.save()  # GUARDAMOS RECIEN AQUI EL REGISTRO
#            return redirect('index')
#    else:
#        form = PrestamoLibroForm()
#
#    context = {'form': form}
#    return render(request, 'libros_prestar.html', context)

"""
    VIEWS ENDPOINT
    BEGINS HERE
"""

def end_libros_todos(request):
    #TRAEMOS TODOS LOS LIBROS
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
    
    #RETORNAMO LA LISTA EN UN JSON
    return JsonResponse(libros_data,safe=False)


def borrar_prestamo_libro(request, id):
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
    

# MOVER LA VIEW A DONDE SE QUIERA ESTA SOLO RENDERIZA UN TEMPLATE PAR ERROR
def error(request):
    return render(request, "error.html") # se agrego la URL