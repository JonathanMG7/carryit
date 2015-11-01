# encoding:utf-8
from .utils import get_timestamp
from random import randint
from django.db.models import Q
from django.db import models
from django.contrib.auth.models import User

ENCOMIENDA = "ENCOMIENDA"
TRAMITE = "TRAMITE"
PENDIENTE = "PENDIENTE"
EN_PROCESO = "EN_PROCESO"
ENTREGADO = "ENTREGADO"
CANCELADO = "CANCELADO"

# cada tupla tiene esta estrucura: (DATO_EN_DB, DATO_MIRA_USUARIO)
TIPO_SOLICITUD = (
    (ENCOMIENDA, 'Encomienda'),
    (TRAMITE, 'Tramite'),
)

ESTADO_SOLICITUD = (
    (PENDIENTE, 'Pendiente'),
    (EN_PROCESO, 'En proceso'),
    (ENTREGADO, 'Entregado'),
    (ENTREGADO, 'Cancelado'),
    )

class SolicitudManager(models.Manager):

    def get_by_client_id(self, client_id):
        return self.filter(id_cliente=client_id, estado="PENDIENTE").values("guia", "dir_origen", "dir_destino")

    def get_by_client_guia(self, guia):
        try:
            return self.get(guia=guia)
        except Exception, e:
            print 'ERROR:', e
            return None

    def get_solicitudes_as_json(self):
        return self.filter(estado="PENDIENTE", mensajero=0).values("guia", "fecha_creacion", "estado")

    def get_solicitudes_as_json_msj(self, id):
        return self.filter(mensajero=id).filter(~Q(estado="ENTREGADO")).values("guia", "dir_origen", "dir_destino")

    def get_solicitudes_as_json_adm(self):
        return self.values("guia", "fecha_creacion", "estado")

class comentarioManager(models.Manager):
    
    def get_comentario_as_json(self, guia):
        return self.filter(guia=guia).values("fecha", "comentario")

class Solicitud(models.Model):
    guia = models.CharField(max_length=20)
    tipo = models.CharField(max_length=20, choices=TIPO_SOLICITUD, default=ENCOMIENDA)
    id_cliente = models.CharField(max_length=20)
    nom_cliente = models.CharField(max_length=50)
    tel_cliente = models.CharField(max_length=20)
    dir_origen = models.CharField(max_length=200)
    dir_destino = models.CharField(max_length=200)
    descripcion = models.TextField()
    observaciones = models.TextField(null=True, blank=True)
    estado = models.CharField(max_length=20, choices=ESTADO_SOLICITUD, default=PENDIENTE)

    fecha_creacion = models.DateTimeField(auto_now_add=True, max_length=15)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    mensajero = models.CharField(max_length=10, default=0)

    objects = SolicitudManager()

    def get_guia(self):
        return self.guia

    def save(self, *args, **kwargs):
        # Se reescribe self.guia solo si no existe un pk
        if self.pk is None:
            # Se contruye el valor de self.guia antes de que se guarde el modelo (linea super)
            r = get_timestamp() + randint(0, 9)
            self.guia = u"{}{}".format(self.tipo[0:1], r)
        # permite que se ejecute el método save de la clase padre "models.Model"
        super(Solicitud, self).save(*args, **kwargs)

    def __unicode__(self):
        # return self.tipo + " - " + self.descripcion[:10]
        return self.guia

class Comentarios(models.Model):
    guia = models.CharField(max_length=20)
    fecha = models.DateTimeField(auto_now_add=True, max_length=15)
    comentario = models.TextField(null=False, blank=True)

    objects = comentarioManager()

    def save(self, *args, **kwargs):
        super(Comentarios, self).save(*args, **kwargs)

    def __unicode__(self):
        # return self.tipo + " - " + self.descripcion[:10]
        return self.guia