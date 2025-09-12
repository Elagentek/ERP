from django.db import models
from Productos.models import Producto

class Venta(models.Model):
    cliente = models.CharField(max_length=150)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)   # 👈 ESTE CAMPO ES NECESARIO
    total = models.DecimalField(max_digits=12, decimal_places=2)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.cliente} - {self.producto.nombre} x {self.cantidad}"
