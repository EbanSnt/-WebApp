from django.contrib import admin

from biblioteca.models import *

# Register your models here.


class AutorAdmin(admin.ModelAdmin):
    # Lista por donde como se muestra en el django admin
    list_display = ('nombre', 'apellido', 'nacionalidad', 'activo')
    # filtro por el cual se puede buscar en el django admin
    list_search = ('nombre', 'apellido')
    # filtro por el cual se puede filtrar en el django admin
    list_filter = ('activo', 'nacionalidad')


admin.site.register(Autor, AutorAdmin)


class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "apellido", "numero_legajo", "activo",)
    list_filter = ('activo',)
    list_search = ('nombre', 'apellido',)


admin.site.register(Empleado, EmpleadoAdmin)


class LibroAdmin(admin.ModelAdmin):
    list_display = ("titulo", "descripcion", "isbn", "autor", "activo")
    list_search = ("titulo",)
    list_filter = ("activo",)


admin.site.register(Libro, LibroAdmin)


class PrestamoAdmin(admin.ModelAdmin):
    list_display = ("socio", "empleado", "libro",
                    "fecha_prestamo", "fecha_devolucion")
    list_search = ('socio', "libro", "empleado")


admin.site.register(Prestamo_libro, PrestamoAdmin)


class SocioAdmin(admin.ModelAdmin):
    list_display = ("nombre", "apellido", "fecha_nacimiento", "activo")
    list_search = ('nombre', "apellido")
    list_filter = ("activo",)


admin.site.register(Socio, SocioAdmin)
