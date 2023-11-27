from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    direccion = models.CharField(max_length=100, default='n/a')
    dni = models.CharField(max_length=8, default='11111111')

    def clean_dni(self):
        if not self.cleaned_data['dni'].isnumeric():
            raise ValidationError("El dni debe ser numerico")

        return self.cleaned_data['dni']
    
    def __str__(self) -> str:
        return f"{self.first_name.capitalize()} {self.last_name.capitalize()} - {self.dni};"
    
    def get_mensualidad_movil(self):
        suma = 0
        actividades = Curso.objects.filter(alumnos = self)

        for i in range(actividades):
            suma += actividades[i].mensualidad
    
        return suma

class Actividad(models.Model):
    nombre = models.CharField(max_length=30, unique=True)

    def __str__(self) -> str:
        return self.nombre
    
    class Meta:
        verbose_name_plural = "actividades"
    
class Predio(models.Model):
    nombre = models.CharField(max_length=40, unique=True)

    def __str__(self) -> str:
        return self.nombre


class Dia(models.Model):
    dia = models.CharField(max_length=9, unique=True)

    def __str__(self) -> str:
        return self.dia

    def clean_dia(self):
        if not self.cleaned_data['dia'] in ["lunes","martes","miercoles","jueves","viernes","sabado","domingo"]:
            raise ValidationError("Dia no pertenece al calendario") 

        return self.cleaned_data['dia']
    

class Curso(models.Model):
    actividad = models.ForeignKey(Actividad, on_delete=models.CASCADE)
    alumnos = models.ManyToManyField(User, through="Inscripcion")
    dias = models.ManyToManyField(Dia, through="DiaCurso")
    desde = models.FloatField()
    hasta = models.FloatField()
    predio = models.ForeignKey(Predio, on_delete=models.DO_NOTHING)
    mensualidad = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.actividad} en {self.predio} dias {[i.dia for i in self.dias.all()]}"

    def clean_horario(self):
        if not(0 < self.cleaned_data['desde'] < 24 and 0 < self.cleaned_data['hasta'] < 24 ):
            raise ValidationError("Fechas incorrectas no cumplen formato de 24hs")
        if not(self.cleaned_data['desde'] < self.cleaned_data['hasta']):
            raise ValidationError("El inicio debe ser menor que el final de la clase")
    
    def clean_mensualidad(self):
        if self.cleaned_data['mensualidad'] < 0:
            raise ValidationError("La mensualidad no puede ser negativa")

        return self.cleaned_data['mensualidad']

class Inscripcion(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    alumno = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha = models.DateField()

    def __str__(self) -> str:
        return f"inscripcion de {self.curso.actividad} en {self.curso.predio} del alumno {self.alumno}"

    class Meta:
        verbose_name_plural = "inscripciones"

class DiaCurso(models.Model):
    curso = models.ForeignKey(Curso,on_delete=models.CASCADE)
    dia = models.ForeignKey(Dia, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"clase de {self.curso.actividad} en {self.curso.predio} el dia {self.dia}"
    

#grupo familiar y pagos
class GrupoFamiliar(models.Model):
    nombre = models.CharField(max_length=50)
    integrantes = models.ManyToManyField(User, through="SocioGrupo")

    def __str__(self) -> str:
        return f'Familia {self.nombre}'
    
    class Meta:
        verbose_name_plural = "grupos familiares"

class SocioGrupo(models.Model):
    grupo = models.ForeignKey(GrupoFamiliar,on_delete=models.CASCADE)
    socio = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.socio} de la familia {self.grupo}"

class Pago(models.Model):
    grupo = models.ForeignKey(GrupoFamiliar, on_delete=models.CASCADE, default=1)
    monto = models.IntegerField()
    fecha = models.DateField()

    def clean_pago(self):
        pass



