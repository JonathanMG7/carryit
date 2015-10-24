# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.contrib.auth import logout
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.http import *
from django.contrib.auth.decorators import login_required
from forms import UserForm, ClientForm, ClientProfile


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
    return render(request, 'login.html', locals())


@login_required
def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST, prefix='user')
        if form.is_valid():
            user = form.save()
            return HttpResponseRedirect("/#{}".format(user.username))
    else:
        form = UserForm(prefix='user')

    return render(request, "signup.html",  {'userform': form})


def singclient(request):
    if request.method == 'POST':
        user_form = ClientForm(request.POST, prefix='user')
        profile_form = ClientProfile(request.POST, prefix='Profile')

        if user_form.is_valid() and profile_form.is_valid():
            user_obj = user_form.save()
            user_profile = profile_form.save(commit=False)
            user_profile.user = user_obj
            user_profile.save()

            login_url = reverse("sign:entrar")
            url_to_redirect = u"{0}?username={1}".format(login_url, user_obj.username)
            return HttpResponseRedirect(url_to_redirect)
    else:
        user_form = ClientForm(prefix='user')
        profile_form = ClientProfile(prefix='Profile')

    ctx = {'clientform': user_form, 'ClientProfile': profile_form}

    return render(request, "regclient.html",  ctx)
