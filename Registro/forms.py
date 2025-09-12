from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegistroUsuario(UserCreationForm):
    username = forms.CharField(
        label="Nombre de usuario",
        error_messages={"required": "Debes ingresar un nombre de usuario"}
    )
    email = forms.EmailField(
        label="Correo electrónico",
        error_messages={"required": "El correo es obligatorio", "invalid": "Correo inválido"}
    )
    password1 = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput,
        error_messages={"required": "Debes ingresar una contraseña"}
    )
    password2 = forms.CharField(
        label="Confirmar contraseña",
        widget=forms.PasswordInput,
        error_messages={"required": "Debes confirmar tu contraseña"}
    )

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
