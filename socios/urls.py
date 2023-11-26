from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('', views.Perfil.as_view(), name='socio-perfil'), 
    # path('socios/nuevo',views.socio_nuevo,name="nuevo_socio"),
    # path('socios/login',views.loginView, name='Socios_login'),
    path('logout', LogoutView.as_view(), name='socio-logout'),
    # path('Portal-socios',views.info_socio,name="info_socio"),
    # path('Portal-socios/reclamo', views.reclamo_socio, name="reclamo_socio"),
    # path('Portal-socios/info', views.info_socio, name="info_socio")

]