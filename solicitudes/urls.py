from django.conf.urls import url
from solicitudes import views

urlpatterns = (
    url(r'^$', views.index, name='index'),
    url(r'^lista/', views.lista, name='lista'),
<<<<<<< HEAD
    url(r'^listas/',views.lista_asJson, name='listas'),
    )
=======
    url(r'^listas/', views.lista_asJson, name='listas'),
)
>>>>>>> a572ff2ce480deebf211bd9e6e24bf01a14ed113
