from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.views.generic import TemplateView
from .forms import LoginForm
from django.http import HttpResponseRedirect
from socios.views import Perfil

# Create your views here.
class Index(TemplateView):
    template_name = "core/index.html"

class Actividades(TemplateView): #a cambiar por una ListView en un futuro
    template_name = "core/actividades.html"

class Contacto(TemplateView):   #a cambiar por lo que corresponda
    template_name = "core/contacto.html"

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