from django import forms

class LoginForm(forms.Form):
    nombre = forms.CharField(label="Nombre de usuario:", required=True)
    clave = forms.CharField(label="Contraseña",widget=forms.PasswordInput, required=False)
