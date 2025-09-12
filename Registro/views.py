from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import RegistroUsuario   # nombre correcto del form


def registro_usuario(request):
    if request.method == "POST":
        form = RegistroUsuario(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("dashboard")
    else:
        form = RegistroUsuario()
    return render(request, "Registro/registro.html", {"form": form})


def login_usuario(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("dashboard")
        else:
            return render(request, "login.html", {"error": "Credenciales inválidas"})
    return render(request, "login.html")

from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Bienvenido a AGROLAT</h1><p>Ir a <a href='/login/'>Login</a> o <a href='/registro/'>Registro</a></p>")
