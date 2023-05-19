from multiprocessing import context
from django.shortcuts import redirect, render
from .forms import *
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
# Create your views here.
#HEADER PRESENTE EN TODAS LAS PAGINAS
def index(request):
    return render(request,"index.jinja2")

def empleado_lista(request):
    try:
        empleados = Empleado.objects.all()

        context = {"empleados": empleados }

        return render(request, "empleado_lista.jinja2", context)
    
    except Exception:

        return render(request, "empleado_lista.jinja2")


#Crea un nuevo empleado y lo guarda en la base de datos
'''def registrar_empleado(request):
    form = EmpleadoForm()
    
    if request.method =="POST":
        form = EmpleadoForm(request.POST)
        if form.is_valid():

            empl = Empleado(
                nombre = form.cleaned_data["nombre"],
                apellido = form.cleaned_data["apellido"],
                numero_legajo = form.cleaned_data["numero_legajo"],
                activo = form.cleaned_data["activo"]
            )

            empl.save()
            return redirect("templates/empleado_lista/")
    else:   
        return redirect("templates/empleado_lista/")
    
    context = { "form": form }

    # renderiza el template cambiar el nombre dependiendo del template
    return render(request, "empleado_nuevo.jinja2", context) '''
@csrf_exempt
def registrar_empleado(request):
    form = EmpleadoForm()
    if request.method == "POST":
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            return redirect("templates/empleado_lista/")
    context = {'form': form}
    return render(request, "empleado_nuevo.jinja2", context)



@csrf_exempt
def actualizar_empleado(request,id):
    """permitir actualizar datos de empleados en el sistema"""
    
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
        return render(request,"empleado_actualizar.jinja2",{"empleado":empleado})
    


def desactivar_empleado(request, id):
    empleado = Empleado.objects.get(id=id)
    if request.method == "POST":
        empleado.activo = False
        empleado.save()
        messages.success(request, "El empleado ha sido desactivado exitosamente.")
        return redirect("empleado_lista")
    else:
        return render(request, "empleado_actualizar.jinja2", {"empleado": empleado})

