from django.contrib import admin

from solicitudes.models import Solicitud, Comentarios


class SolicitudAdmin(admin.ModelAdmin):
	list_display = ['guia', 'nom_cliente', 'estado', 'fecha_creacion']

class ComentarioAdmin(admin.ModelAdmin):
	list_display = ['guia', 'fecha']


admin.site.register(Solicitud, SolicitudAdmin)
admin.site.register(Comentarios, ComentarioAdmin)

# Register your models here.
