from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.Index.as_view(), name='index'), 
    path('actividades',views.Actividades.as_view(), name='core-actividades'),
    path('preguntas_frecuentes',views.FAQ.as_view(), name='core-faq'),
    path('institucional',views.Institucional.as_view(), name='core-institucional'),
    # path('actividades/<str:actividad>', views.actividad, name="detalle_actividad"),
    path('contacto',views.Contacto.as_view(),name="core-contacto"),
    # path('listado_actividades',views.ListaActividades.as_view(),name="lista_actividad"),
    path('login', views.loginView, name = "login"),
    path('miPerfil/', include('socios.urls'))
]