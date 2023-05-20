from django import forms
from .models import *


class EmpleadoForm(forms.ModelForm):
    class Meta():
        model = Empleado
        fields = '__all__'
        widgets={"nombre":forms.TextInput(attrs={"class":"form-control my-3"}),
                 "apellido":forms.TextInput(attrs={"class":"form-control my-3"}),
                 "numero_legajo":forms.TextInput(attrs={"class":"form-control my-3","type":"number"}),
                 "activo":forms.CheckboxInput(attrs={"class":"form-check-input my-2"})
                 }
 