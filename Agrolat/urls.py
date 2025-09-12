from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path("admin/", admin.site.urls),
    path("login/", include("Login.urls")),      # 👈 aquí está incluido Login
    path("registro/", include("Registro.urls")),
    path("dashboard/", include("Dashboard.urls")),
    path("", lambda request: redirect("login")),  # raíz → login
    path("productos/", include("Productos.urls")),
    path('ventas/', include('Ventas.urls')),   # ✅ nuevo


]
