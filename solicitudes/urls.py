from django.conf.urls import include, url
from django.conf.urls import patterns, url
from solicitudes import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    
]