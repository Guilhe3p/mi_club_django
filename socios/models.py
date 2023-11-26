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

