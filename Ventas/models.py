from django.db import models
from Productos.models import Producto

class Venta(models.Model):
    TIPO_VENTA = [
        ("FISICA", "Física / Mostrador"),
        ("PEDIDO", "Pedido / Con despacho"),
    ]
    ESTADO_VENTA = [
        ("PENDIENTE", "Pendiente"),
        ("ENTREGADO", "Entregado"),
        ("CANCELADO", "Cancelado"),
    ]

    cliente = models.CharField(max_length=100)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    total = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateTimeField(auto_now_add=True)

    # Campos nuevos
    tipo = models.CharField(max_length=10, choices=TIPO_VENTA, default="FISICA")
    estado = models.CharField(max_length=20, choices=ESTADO_VENTA, default="PENDIENTE")
    fecha_entrega = models.DateField(null=True, blank=True)
    direccion = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.cliente} - {self.producto.nombre} ({self.tipo})"
