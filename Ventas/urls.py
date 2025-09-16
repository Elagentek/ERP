from django.urls import path
from . import views

urlpatterns = [
    path('', views.ventas_list, name='ventas_list'),
]
