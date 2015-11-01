# encoding:utf-8
from django.shortcuts import render, render_to_response
from django.http import JsonResponse
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from forms import SolicitudForm, ListaSolicitudes, SolicitudFormModif, CambiaEstado, NuevoComent
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt
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

def lista_asJsonAdm(request):
    datos = Solicitud.objects.get_solicitudes_as_json_adm()
    data_to_jdt = {'data': list(datos)}
    return JsonResponse(data_to_jdt, safe=False)


def lista_asJson_msj(request):
    userpk = request.user.pk
    dato = Solicitud.objects.get_solicitudes_as_json_msj(userpk)
    data_to_jdt_msj = {'data': list(dato)}
    return JsonResponse(data_to_jdt_msj, safe=False)

@login_required
def lista(request):
    return render(request, 'lista.html', locals())

@login_required
def listaAdmin(request):
    return render(request, 'listacompleta.html', locals())

@login_required
def lista_msj(request):
    return render(request, 'listapendientes.html', locals())

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
    return render(request, 'get_guia.html', locals())

def asignarme(request):
    guia = request.GET.get("busqueda")
    mod = Solicitud.objects.get(guia=guia)
    userpk = request.user.pk
    if request.method =='POST':
        form = SolicitudFormModif(request.POST,request.FILES)
        if form.is_valid():
            tipo = form.cleaned_data['tipo']
            guia = form.cleaned_data['guia']
            dir_origen = form.cleaned_data['dir_origen']
            dir_destino = form.cleaned_data['dir_destino']
            descripcion = form.cleaned_data['descripcion']
            mensajero = form.cleaned_data['mensajero']
            mod.tipo = tipo
            mod.guia = guia
            mod.dir_origen = dir_origen
            mod.dir_destino = dir_destino
            mod.descripcion = descripcion
            mod.mensajero = mensajero
            mod.save()
            return HttpResponseRedirect('/solicitudes/lista/')
    if request.method == 'GET':
        form = SolicitudFormModif(initial={
                                'tipo':mod.tipo,
                                'guia':mod.guia,
                                'dir_origen':mod.dir_origen,
                                'dir_destino':mod.dir_destino,
                                'descripcion':mod.descripcion,
                                'mensajero':userpk

            })
    ctx = {'form': form, 'Solicitud': mod}
    return render(request, "asignarme.html",  ctx)

def cambiaestado(request):
    guia = request.GET['busqueda']
    mod = Solicitud.objects.get(guia=guia)
    variable = mod.guia
    if request.method =='POST':
        form = CambiaEstado(request.POST,request.FILES)
        form2 = NuevoComent(request.POST)
        if form.is_valid() and form2.is_valid():
            tipo = form.cleaned_data['tipo']
            guia = form.cleaned_data['guia']
            dir_origen = form.cleaned_data['dir_origen']
            dir_destino = form.cleaned_data['dir_destino']
            observaciones = form.cleaned_data['observaciones']
            estado = form.cleaned_data['estado']
            mod.tipo = tipo
            mod.guia = guia
            mod.dir_origen = dir_origen
            mod.dir_destino = dir_destino
            mod.observaciones = observaciones
            form2.comentario = observaciones
            mod.estado = estado
            mod.save()
            if request.POST['comentario'] != "":
                com = form2.save()
            return HttpResponseRedirect('/solicitudes/listas_msj/')
    else:
        form2= NuevoComent()
    if request.method == 'GET':
        form = CambiaEstado(initial={
                                'tipo':mod.tipo,
                                'guia':mod.guia,
                                'dir_origen':mod.dir_origen,
                                'dir_destino':mod.dir_destino,
                                'observaciones':mod.observaciones,
                                'estado':mod.estado

            })
    
    ctx = {'form': form, 'Solicitud': mod}
    return render(request, "aentrega.html",  locals())

def get_comentario_asJson(request):
    b = request.GET.get('buscar')
    # b = "E1444628579"
    data = Comentarios.objects.get_comentario_as_json(b)
    data_to_jdt = {'data': list(data)}
    return JsonResponse(data_to_jdt, safe=False)