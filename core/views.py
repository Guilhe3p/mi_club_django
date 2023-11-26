from django.shortcuts import render
from django.template import loader
from django.views.generic import TemplateView

# Create your views here.
class Index(TemplateView):
    template_name = "core/index.html"

class Actividades(TemplateView): #a cambiar por una ListView en un futuro
    template_name = "core/actividades.html"

class Contacto(TemplateView):   #a cambiar por lo que corresponda
    template_name = "core/contacto.html"