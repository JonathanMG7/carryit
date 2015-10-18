from django.shortcuts import render
from django.contrib.auth import logout
from django.shortcuts import render_to_response, RequestContext
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.http import *
from django.shortcuts import render_to_response,redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from forms import UserForm
from django.contrib.auth.forms import UserCreationForm


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

@login_required
def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST, prefix='user')
        if form.is_valid():
            user = form.save()
            return HttpResponseRedirect("/#")
    else:
        form = UserForm(prefix='user')
    # return render_to_response('signup.html',  dict(userform=form, context_instance=RequestContext(request)))


    return render_to_response("signup.html",  {'userform': form,  }, context_instance = RequestContext(request))