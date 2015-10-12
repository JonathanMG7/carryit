from django.conf.urls import url
from solicitudes import views

urlpatterns = (
    url(r'^$', views.index, name='index'),
    url(r'^lista/', views.lista, name='lista'),
    url(r'^listas/', views.lista_asJson, name='listas'),
)