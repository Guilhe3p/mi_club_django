from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('', views.Perfil.as_view(), name='socio-perfil'), 
    path('grupo',views.GrupoFamiliar.as_view(), name='socio-grupo_familiar'),
    path('logout', LogoutView.as_view(), name='socio-logout'),
    path('pagos',views.HistorialPagos.as_view(),name="socio-pagos"),
    # path('Portal-socios/reclamo', views.reclamo_socio, name="reclamo_socio"),
    path('noticias', views.NoticiasView.as_view(), name="noticias")

]