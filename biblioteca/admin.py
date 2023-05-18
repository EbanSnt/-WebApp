from django.contrib import admin

# Register your models here.
from .models import Empleado
# Register your models here.
class MemberAdmin(admin.ModelAdmin):
  list_display = ("nombre", "apellido", "numero_legajo","activo",)
  list_filter = ('activo',)
  list_search = ('nombre', 'apellido',)

admin.site.register(Empleado, MemberAdmin)