from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.forms.widgets import PasswordInput, TextInput

class CustomPwdChgForm(PasswordChangeForm):
    old_password = forms.CharField(widget=TextInput(attrs={'placeholder': 'Contraseña anterior', 'class':'form-control'}))
    new_password1 = forms.CharField(widget=TextInput(attrs={'placeholder': 'Nueva contraseña', 'class':'form-control'}))
    new_password2 = forms.CharField(widget=TextInput(attrs={'placeholder': 'Repetir nueva contraseña', 'class':'form-control'}))

    