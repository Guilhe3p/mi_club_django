from django.shortcuts import render
from django.template import loader
from django.views.generic import TemplateView, ListView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *

# Create your views here.onclick=location.href="{% url 'info_socio' %}"><i class="fas fa-info-circle"></i><span class="m-2">INFORMACION</span>
class Perfil(LoginRequiredMixin, View):
    template_name = "socios/perfil.html"
    model = User
    context_object_name = 'datos_socio'

    def get(self, request):
        context = {
            'socio' : User.objects.filter(id = self.request.user.id)[0]
        }
        return render(request,self.template_name,context)
