# encoding:utf-8
from django.shortcuts import render, render_to_response
from django.http import JsonResponse
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from forms import SolicitudForm, ListaSolicitudes
from django.core.context_processors import csrf
from django.db import connection
from solicitudes.models import Solicitud
from django.core import serializers
from models import *


# Create your views here.
def index(request):
    if request.POST:
        form = SolicitudForm(request.POST)
        if form.is_valid():
            solicitud = form.save()
            messages.success(request, "Su solicitud ha sido creada.<br><br>En breve uno de nuestros mensajeros lo estara visitando para atender la solicitud")
            messages.warning(request, "Su numero de guia es: {} Por favor conservelo, ya que sera necesario para futuras reclamaciones".format(solicitud.get_guia()))
            return HttpResponseRedirect("confirm")
    else:
        form = SolicitudForm()

    return render(request, 'index.html', locals())


def lista_asJson(request):

    data = Solicitud.objects.get_solicitudes_as_json()

    # la estructura json que espera jQuery.dataTable es: [{"data": []}]
    data_to_jdt = {'data': list(data)}

    # JsonResponse convierte una estructura python en json para enviarselo a la respuesta http
    return JsonResponse(data_to_jdt, safe=False)


@login_required
def lista(request):
    return render(request, 'lista.html', locals())


def confirm(request):
    return render(request, 'confirm.html', locals())

def get_guia_asJson(request):
    b = request.GET.get("busqueda")
    data = Solicitud.objects.get_by_client_guia(b)
    data_to_jdt = {'data': list(data)}
    return JsonResponse(data_to_jdt, safe=False)

    
def get_guia(request):
    b = request.GET.get("busqueda")
    solicitud = Solicitud.objects.get_by_client_guia(b)
    #c = solicitud.estado
    # return HttpResponse(solicitud)
    return render(request, 'get_guia.html', locals())