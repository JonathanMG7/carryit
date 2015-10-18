from django.shortcuts import render
from django.contrib.auth import logout
from django.shortcuts import render_to_response, RequestContext
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.http import *
from django.shortcuts import render_to_response,redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required


# Create your views here.
def logoutView(request):
    logout(request)
    return HttpResponseRedirect("/#")

def loginView(request):
    logout(request)
    username = password = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/#')
    return render_to_response('login.html', context_instance=RequestContext(request))