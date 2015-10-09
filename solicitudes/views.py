from django.shortcuts import render, render_to_response, RequestContext
from django.http import HttpResponse
from django.template import RequestContext, loader

# Create your views here.
def index(request):
	return render(request, "index.html", locals())

