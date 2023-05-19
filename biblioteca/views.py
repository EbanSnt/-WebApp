from django.shortcuts import redirect, render
from .forms import *
# Create your views here.
#HEADER PRESENTE EN TODAS LAS PAGINAS
def index(request):
    return render(request,"index.jinja2")

def registrar_empleado(request):
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
            return redirect("biblioteca/empleado_lista/")
    else:   
        return redirect("biblioteca/empleado_lista/")
    
    context = { "form": form }

    # renderiza el template cambiar el nombre dependiendo del template
    return render(request, "empleado_form.html", context) 