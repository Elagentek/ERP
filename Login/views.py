from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.contrib.auth import logout



def login_usuario(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("dashboard")
        else:
            return render(request, "Login/login.html", {"error": "Credenciales inválidas"})
    return render(request, "Login/login.html")




def home(request):
    return HttpResponse(
        "<h1>Bienvenido a AGROLAT</h1>"
        "<p>Ir a <a href='/login/'>Login</a> o <a href='/registro/'>Registro</a></p>"
    )

def logout_usuario(request):
    logout(request)
    return redirect("login")   # aquí vuelve al login después de cerrar sesión