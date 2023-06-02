from django import forms
from .models import *


class EmpleadoForm(forms.ModelForm):
    class Meta():
        model = Empleado
        fields = '__all__'
        widgets={"nombre":forms.TextInput(attrs={"class":"form-control my-3"}),
                 "apellido":forms.TextInput(attrs={"class":"form-control my-3"}),
                 "numero_legajo":forms.NumberInput(attrs={"class":"form-control my-3","type":"number"}),
                 "activo":forms.CheckboxInput(attrs={"class":"form-check-input my-2"})
                 }
 

class AutoresForm(forms.ModelForm):
    class Meta():
        model = Autor
        fields = '__all__'
        widgets = {
            "nombre": forms.TextInput(attrs={"class":"form-control my-3"}),
            "apellido": forms.TextInput(attrs={"class":"form-control my-3"}),
            "nacionalidad": forms.TextInput(attrs={"class":"form-control my-3"}),
            "activo": forms.CheckboxInput(attrs={"class":"form-check-input my-2"})
        }

class SociosForm(forms.ModelForm):
    class Meta():
        model = Socio
        fields = '__all__'
        widgets = {
            "nombre": forms.TextInput(attrs={"class":"form-control my-3"}),
            "apellido": forms.TextInput(attrs={"class":"form-control my-3"}),
            "fecha_nacimiento": forms.DateInput(attrs={"class":"form-control my-3","type":"date"}),
            "activo": forms.CheckboxInput(attrs={"class":"form-check-input my-2"})
        }

class PrestamoLibroForm(forms.ModelForm):
    fecha_devolucion = forms.DateField(
        widget=forms.HiddenInput(),
        required=False
    )
    class Meta():
        model = Prestamo_libro
        fields = '__all__'
        widgets = {
            "socio": forms.Select(attrs={"class":"form-control my-3"}),
            "libro": forms.Select(attrs={"class":"form-control my-3"}),
            "empleado": forms.Select(attrs={"class":"form-control my-3"}),
            "fecha_prestamo": forms.DateInput(attrs={"class":"form-control my-3", "type":"date"}),
            "fecha_devolucion": forms.DateInput(attrs={"class":"form-control my-3", "type":"date"}),
        }

class LibroForm(forms.ModelForm):
    class Meta():
        model = Libro
        fields = '__all__'
        widgets={"titulo":forms.TextInput(attrs={"class":"form-control my-3"}),
                 "descripcion":forms.TextInput(attrs={"class":"form-control my-3"}),
                 "isbn":forms.NumberInput(attrs={"class":"form-control my-3","type":"number"}),
                 "autor": forms.Select(attrs={"class":"form-control my-3"}),
                 "activo":forms.CheckboxInput(attrs={"class":"form-check-input my-2"})
                 }