from django.shortcuts import redirect, render

# Create your views here.

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
            return redirect("/empleado_lista/")
    else:   
        return redirect("/empleado_lista/")
    context = { "form": form }

    return render(request, "empleado_form.html", context)