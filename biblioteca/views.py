from django.shortcuts import redirect, render
from .forms import *
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages



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
    if request.method == "POST":
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("empleado_lista")   # añadido redireccion al listado para cargar el nuevo 
        else:
            return redirect("empleado_lista")
    context = {'form': form}
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


def desactvar_autor(request, id):
    autor = Autor.objects.get(id = id)
    if request.method =="POST":
        autor.activo = False
        autor.save()
        messages.success(request, "El Autor ha sido desactivado exitosamente")
        return redirect("autor_lista")
    else:
        return render(request, "autor_actulizar.html", {"autor": autor})