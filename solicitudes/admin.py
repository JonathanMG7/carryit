from django.contrib import admin

from solicitudes.models import Solicitud


class SolicitudAdmin(admin.ModelAdmin):
	list_display = ['guia', 'nom_cliente', 'estado', 'fecha_creacion']


admin.site.register(Solicitud, SolicitudAdmin)

# Register your models here.
