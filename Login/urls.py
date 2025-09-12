from django.urls import path
from . import views

urlpatterns = [
    path("", views.login_usuario, name="login"),
    path("logout/", views.logout_usuario, name="logout"),  # 👈 ruta logout
]
