from django.urls import path
from . import views

urlpatterns = [
    path("", views.productos_crud, name="productos"),
]
