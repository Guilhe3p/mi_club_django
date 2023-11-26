from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.Index.as_view(), name='index'), 
    path('actividades',views.Actividades.as_view(), name='actividades'),
    # path('institucional',views.institucional, name='AppMyClub_institucional'),
    # path('actividades/<str:actividad>', views.actividad, name="detalle_actividad"),
    path('contacto',views.Contacto.as_view(),name="contacto"),
    # path('listado_actividades',views.ListaActividades.as_view(),name="lista_actividad"),
    path('miPerfil/', include('socios.urls'))
]