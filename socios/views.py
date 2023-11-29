from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from .forms import CustomPwdChgForm
from .models import *


# Create your views here.onclick=location.href="{% url 'info_socio' %}"><i class="fas fa-info-circle"></i><span class="m-2">INFORMACION</span>
class Perfil(LoginRequiredMixin, View):
    template_name = "socios/perfil.html"
    model = User
    context_object_name = 'datos_socio'

    def get(self, request):
        context = {
            'socio' : request.user
        }
        return render(request,self.template_name,context)
    
class GrupoFamiliar(Perfil):
    template_name = "socios/grupo_familiar.html"

class HistorialPagos(Perfil):
    template_name = "socios/pagos.html"

class NoticiasView(ListView):
    model = Comunicado
    template_name = "socios/noticias.html"
    context_object_name = 'noticias'
    ordering = ['-fecha']

class CambiarContra(PasswordChangeView):
    template_name = "socios/cambiar_clave.html"
    form_class = CustomPwdChgForm
    success_url = 'miPerfil'
    
