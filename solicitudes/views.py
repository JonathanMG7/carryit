from django.shortcuts import render, render_to_response, RequestContext
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import RequestContext, loader
from forms import SolicitudForm, ListaSolicitudes
from django.core.context_processors import csrf
from django.db import connection
from django.contrib import messages
from solicitudes.models import Solicitud
from django.core import serializers
import json
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

	data = Solicitud.objects.all()
	json = serializers.serialize("json", data)
	return HttpResponse(json, content_type='application/json')

def lista(request):
	return render(request, 'lista.html', locals())