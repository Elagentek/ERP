from django.shortcuts import render, redirect, get_object_or_404
from .models import Venta
from .forms import VentaForm
from Productos.models import Producto
from django.db.models import Sum

def ventas_list(request):
    ventas = Venta.objects.all()

    # Métricas
    total_ventas = ventas.count()
    ingresos_totales = ventas.aggregate(Sum('total'))['total__sum'] or 0
    productos_vendidos = ventas.aggregate(Sum('cantidad'))['cantidad__sum'] or 0

    form = VentaForm()

    if request.method == 'POST':
        form = VentaForm(request.POST)
        if form.is_valid():
            venta = form.save(commit=False)

            # Calcular total según precio del producto
            venta.total = venta.producto.precio * venta.cantidad

            # Restar del stock del producto
            producto = venta.producto
            if producto.stock >= venta.cantidad:
                producto.stock -= venta.cantidad
                producto.save()
                venta.save()
                return redirect('ventas')  # vuelve a la lista
            else:
                form.add_error('cantidad', 'Stock insuficiente')

    context = {
        'ventas': ventas,
        'form': form,
        'total_ventas': total_ventas,
        'ingresos_totales': ingresos_totales,
        'productos_vendidos': productos_vendidos,
    }
    return render(request, 'Ventas/ventas.html', context)


# ✅ Nueva vista para registrar venta (desde URL /ventas/registrar/)
def registrar_venta(request):
    if request.method == 'POST':
        form = VentaForm(request.POST)
        if form.is_valid():
            venta = form.save(commit=False)
            venta.total = venta.producto.precio * venta.cantidad

            # Restar stock
            producto = venta.producto
            if producto.stock >= venta.cantidad:
                producto.stock -= venta.cantidad
                producto.save()
                venta.save()
                return redirect('ventas')
            else:
                form.add_error('cantidad', 'Stock insuficiente')
    else:
        form = VentaForm()

    return render(request, 'Ventas/registrar.html', {'form': form})
