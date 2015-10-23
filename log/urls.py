from django.conf.urls import url
from log import views


urlpatterns = [
    # url(r'^in/', include(admin.site.urls)),
    url(r'^out/', views.logoutView, name='salir'),
    url(r'^in/', views.loginView, name='entrar'),
    url(r'^up/', views.signup, name='registrar'),
    url(r'^client/', views.singclient, name='registrarcliente')
]
