from django.contrib import admin
from django import forms
from django.contrib.auth.models import Group
from .models import *


#Register your models here.
admin.site.register(Curso)
admin.site.register(Predio)
admin.site.register(Actividad)
admin.site.register(Inscripcion)
admin.site.register(DiaCurso)
admin.site.register(GrupoFamiliar)
admin.site.register(SocioGrupo)
admin.site.register(Pago)
admin.site.register(CambioMensualidadFija)
admin.site.register(Categoria)
admin.site.register(Comunicado)



admin.site.index_title = "Tablas"
admin.site.site_header = "Administración del clu"
admin.site.site_title = "El super clú"




    


'''Agregar socio a grupo familiar existente'''
class AgregarSocioForm(forms.ModelForm):
    grupo = forms.ModelChoiceField(GrupoFamiliar.objects)

    class Meta:
        model = User
        fields = ['first_name','last_name','dni','direccion','email']


@admin.register(User)
class SocioAdmin(admin.ModelAdmin):
    form = AgregarSocioForm
    list_display = ('username', 'first_name', 'last_name', 'dni', 'email', 'direccion')

    def save_model(self, request, obj, form, change):
        #modifico el username y guardo el usuario
        obj.username = username=form.cleaned_data['dni']
        obj.set_password(form.cleaned_data['dni'])      
        super().save_model(request, obj, form, change)

        #si existe el grupo familiar añado al usuario de otra forma creo uno nuevo
        if form.cleaned_data['grupo'].nombre == "nueva":
            permisos = Group.objects.get(name='administrador_grupo_f') 
            permisos.user_set.add(obj)

            grupo_familiar = GrupoFamiliar(nombre=form.cleaned_data['last_name'])
            grupo_familiar.save()
        else:
            permisos = Group.objects.get(name='integrante_grupo_f') 
            permisos.user_set.add(obj)
            grupo_familiar = form.cleaned_data['grupo']

        nuevo_socio_grupo =  SocioGrupo(grupo = grupo_familiar, socio = obj)
        nuevo_socio_grupo.save()