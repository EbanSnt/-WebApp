from django.contrib import admin

from exportcsv.models import HistorialForm

# Register your models here.


class HistorialAdmin(admin.ModelAdmin):
    # Lista por donde como se muestra en el django admin
    list_display = ('fecha', 'descripcion', 'tipo')
    # filtro por el cual se puede buscar en el django admin
    list_search = ('tipo',)
    # filtro por el cual se puede filtrar en el django admin
    list_filter = ('tipo',)


admin.site.register(HistorialForm, HistorialAdmin)
