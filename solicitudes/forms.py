from django import forms
from solicitudes.models import Solicitud


class SolicitudForm(forms.ModelForm):

    class Meta:
        model = Solicitud
        fields = ['tipo', 'id_cliente', 'nom_cliente', 'tel_cliente', 'dir_origen', 'dir_destino', 'descripcion']


class ListaSolicitudes(forms.ModelForm):

    class Meta:
        model = Solicitud
        fields = ['tipo', 'id_cliente', 'dir_origen', 'dir_destino', 'descripcion', 'observaciones', 'estado']

class SolicitudFormModif(forms.ModelForm):

    class Meta:
        model = Solicitud
        fields = ['tipo', 'guia', 'dir_origen', 'dir_destino', 'descripcion', 'mensajero']

class CambiaEstado(forms.ModelForm):

    class Meta:
        model = Solicitud
        fields = ['tipo', 'guia', 'dir_origen', 'dir_destino', 'observaciones', 'estado']