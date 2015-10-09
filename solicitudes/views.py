from django.shortcuts import render, render_to_response, RequestContext
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import RequestContext, loader
from forms import SolicitudForm
from django.core.context_processors import csrf
import MySQLdb

# Create your views here.
def index(request):
    if request.POST:
        form = SolicitudForm(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect("#")
    else:
        form = SolicitudForm()

    args = {}
    args.update(csrf(request))

    args['form'] = form

    return render_to_response('index.html', args)

def listar(request):
	Publisher.objects.all()
	[<Publisher: Addison-Wesley>, <Publisher: O'Reilly>, <Publisher: Apress Publishing>]
