from django import forms
from .models import *


class EmpleadoForm(forms.ModelForm):
    class Meta():
        model = Empleado
        fields = '__all__'
