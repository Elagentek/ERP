# Ventas/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.ventas_list, name='ventas_list'),
    path('registrar/', views.registrar_venta, name='registrar_venta'),
]
