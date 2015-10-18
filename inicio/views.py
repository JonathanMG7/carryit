from django.shortcuts import render, render_to_response, RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.contrib.auth import logout
# Create your views here.

def inicio(request):
	return render(request, 'inicio.html', locals())