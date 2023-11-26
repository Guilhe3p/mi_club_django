from django.contrib import admin
from django import forms
from .models import User, Curso, Predio, Actividad, Inscripcion, DiaCurso, Dia


#Register your models here.
admin.site.register(Curso)
admin.site.register(Predio)
admin.site.register(Actividad)
admin.site.register(Inscripcion)
admin.site.register(DiaCurso)
admin.site.register(Dia)
admin.site.register(User)


admin.site.index_title = "Tablas"
admin.site.site_header = "Administración del clu"
admin.site.site_title = "El super clú"