from tkinter import Widget
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
 

class AutoresForm(forms.ModelForm):
    model = Autor
    field = '__all__'
    widgets = {
        "nombre": forms.TextInput(attrs={"class":"form-control my-3"}),
        "apellido": forms.TextInput(attrs={"class":"form-cotrol my-3"}),
        "nacionalidad": forms.TextInput(attrs={"class":"form-control my-3"}),
        "activo": forms.CheckboxInput(attrs={"class":"form-check-input my-3"})
    }

class SociosForm(forms.ModelForm):
    model = Socio
    field = '__all__'
    widgets = {
        "nombre": forms.TextInput(attrs={"class":"form-control my-3"}),
        "apellido": forms.TextInput(attrs={"class":"form-cotrol my-3"}),
        "fecha_nacimiento": forms.DateInput(attrs={"class":"form-control my-3"}),
        "activo": forms.CheckboxInput(attrs={"class":"form-check-input my-3"})
    }
