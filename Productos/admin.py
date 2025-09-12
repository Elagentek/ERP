from django.contrib import admin
from .models import Producto

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "precio", "stock", "creado_en", "actualizado_en")
    search_fields = ("nombre",)
    list_filter = ("creado_en",)
