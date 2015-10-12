# encoding:utf-8
from django.shortcuts import render, render_to_response
from django.http import JsonResponse
from django.http import HttpResponseRedirect

from forms import SolicitudForm, ListaSolicitudes
from django.core.context_processors import csrf
from django.db import connection
from solicitudes.models import Solicitud
from django.core import serializers
from models import *


cursor = connection.cursor()


# Create your views here.
def index(request):
    if request.POST:
        create = SolicitudForm(request.POST)
        if create.is_valid():
            create.save()

            return HttpResponseRedirect("#")
    else:
        create = SolicitudForm()

    args = {}
    args.update(csrf(request))

    args['form'] = create

    return render_to_response('index.html', args)


def lista_asJson(request):

    # data = Solicitud.objects.all()
    # json_data = serializers.serialize("json", data)
    # Pilas que tenia definida una variable 'json', y arriba estaba importado el módulo json

    # values hace que los datos se retornen como un diccionario python, no como objetos tipo Solicitud
    data = Solicitud.objects.all().values("dir_origen", "tipo", "nom_cliente", "dir_destino", "estado")

    # la estructura json que espera jQuery.dataTable es: [{"data": []}]
    data_to_jdt = {'data': list(data)}

    # JsonResponse convierte una estructura python en json para enviarselo a la respuesta http
    return JsonResponse(data_to_jdt, safe=False)


def lista(request):
    return render(request, 'lista.html', locals())
