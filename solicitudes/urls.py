from django.conf.urls import url
from solicitudes import views

urlpatterns = (
    url(r'^$', views.index, name='index'),
    url(r'^lista/', views.lista, name='lista'),
    url(r'^listas/', views.lista_asJson, name='listas'),
    url(r'^confirm/', views.confirm, name='confirm'),
    url(r'^busca/get_guias/', views.get_guia_asJson, name='get_guias'),
    url(r'^busca/get_guia/', views.get_guia, name='get_guia')
)
