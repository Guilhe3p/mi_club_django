from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.views.generic import TemplateView
from .forms import LoginForm
from django.http import HttpResponseRedirect, Http404
from socios.views import Perfil

# Create your views here.
class Index(TemplateView):
    template_name = "core/index.html"

variable_contexto = {
        'hola' : "1",
        'menu_sports' : [
            {'name':'fútbol','url_image':'core/img/pibe_pelota.jpg'},
            {'name':'voley','url_image':'core/img/volley.jpg'},
            {'name':'basket','url_image':'core/img/basketball.jpg'},
            {'name':'tenis','url_image':'core/img/tenis.jpg'},
            {'name':'natación','url_image':'core/img/natacion.jpg'},
            {'name':'handball','url_image':'core/img/handball.jpg'}
        ],
        'menu_activities' : [
            {'name':'yoga','url_image':'core/img/yoga.jpg'},
            {'name':'expresión','url_image':'core/img/expresion.jpeg'},
            {'name':'parrilla','url_image':'core/img/parrilla.jpeg'},
            {'name':'colonia','url_image':'core/img/colonia.jpg'},
            {'name':'eventos','url_image':'core/img/recital.jpg'},
            {'name':'salón','url_image':'core/img/salon.jpeg'}
        ]
    }

class Contacto(TemplateView):   #a cambiar por lo que corresponda
    template_name = "core/contacto.html"

class Institucional(TemplateView):
    template_name = "core/institucional.html"

class FAQ(TemplateView):
    template_name = "core/faq.html"

class Actividad(TemplateView):
    template_name = "core/actividad.html"

def actividades(request):
    return render(request,"core/actividades.html",variable_contexto)

def actividad(request, actividad):
    # actividad = request.GET.get(actividad)
    print("actividad")
    if actividad in variable_contexto:
        nuevo_contexto = {'actividad':variable_contexto[actividad]}
        return render(request,"core/actividad.html",nuevo_contexto)
    else:
        raise Http404

def loginView(request):
    if request.method == "POST":

        # login_form = LoginForm(request.POST)
  
        # if login_form.is_valid():
        usuario = request.POST['username']
        clave = request.POST['password']

        user = authenticate(request, username = usuario, password = clave)

        if(user is not None):

            login(request,user)

            messages.info(request, "Ha iniciado sesión correctamente")

            return HttpResponseRedirect('/miPerfil')
        else:
            messages.info(request, "Error al iniciar sesion")
            return redirect(reverse('login'))

    else: 
        if request.user.is_authenticated:
            return HttpResponseRedirect('/miPerfil')

        else:
            # context = {
            #     'ingreso_socios': LoginForm()
            # }
            return render(request, 'core/login.html')