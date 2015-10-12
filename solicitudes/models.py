from django.db import models

ENCOMIENDA = "ENCOMIENDA"
TRAMITE = "TRAMITE"
PENDIENTE = "PENDIENTE"
EN_PROCESO = "EN_PROCESO"
ENTREGADO = "ENTREGADO"

# cada tupla tiene esta estrucura: (DATO_EN_DB, DATO_MIRA_USUARIO)
TIPO_SOLICITUD = (
    (ENCOMIENDA, 'Encomienda'),
    (TRAMITE, 'Tramite'),
)

ESTADO_SOLICITUD = (
    (PENDIENTE, 'Pendiente'),
    (EN_PROCESO, 'En proceso'),
    (ENTREGADO, 'Entregado'),
    )

class Solicitud(models.Model):
    tipo = models.CharField(max_length=20, choices=TIPO_SOLICITUD, default=ENCOMIENDA)
    id_cliente = models.CharField(max_length=20)
    nom_cliente = models.CharField(max_length=50)
    tel_cliente = models.CharField(max_length=20)
    dir_origen = models.CharField(max_length=200)
    dir_destino = models.CharField(max_length=200)
    descripcion = models.TextField()
    observaciones = models.TextField(null=True, blank=True)
    estado = models.CharField(max_length=20, choices=ESTADO_SOLICITUD, default=PENDIENTE)

    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __unicode__(self):
    	# return self.tipo + " - " + self.descripcion[:10]
    	return "{}{}".format(self.tipo[0:1], self.pk)

