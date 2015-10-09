from django import forms
from solicitudes.models import Solicitud

class SolicitudForm(forms.ModelForm):

   class Meta:
      model = Solicitud
      fields = [ 'tipo', 'id_cliente', 'nom_cliente', 'tel_cliente', 'dir_origen', 'dir_destino', 'descripcion']
