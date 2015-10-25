from django.conf.urls import url
from solicitudes import views

urlpatterns = (
    url(r'^$', views.index, name='index'),
    url(r'^asignarme/', views.asignarme, name='asignarme'),
    url(r'^cambiarestado/', views.cambiaestado, name='cambiaestado'),
    url(r'^busca/get_guias/', views.get_guia_asJson, name='get_guias'),
    url(r'^busca/get_guia/', views.get_guia, name='get_guia'),
    url(r'^confirm/', views.confirm, name='confirm'),
    url(r'^lista/', views.lista, name='lista'),
    url(r'^listas/', views.lista_asJson, name='listas'),
    url(r'^listaadminjs/', views.lista_asJsonAdm, name='listaadminjs'),
    url(r'^admin/lista/', views.listaAdmin, name='listaAdmin'),
    url(r'^listasmsj/', views.lista_asJson_msj, name='listasmsj'),
    url(r'^listas_msj/', views.lista_msj, name='listas_msj'),
)
