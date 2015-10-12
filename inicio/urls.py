from django.conf.urls import include, url
from django.conf.urls import patterns, url
from inicio import views

urlpatterns = (
    url(r'^$', views.inicio, name='inicio'),

    )