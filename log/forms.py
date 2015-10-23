# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from log.models import UserProfile


class UserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'groups')


class ClientForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('first_name', 'username', 'email', 'password1', 'password2')


class ClientProfile(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ['user']
