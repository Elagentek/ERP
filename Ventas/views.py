from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Sum
from collections import defaultdict

from .models import Venta
from .forms import VentaForm

def ventas_list(request):
    ventas = Venta.objects.all().order_by('-fecha')

    # Agrupar por cliente
    ventas_por_cliente = defaultdict(list)
    for v in ventas:
        ventas_por_cliente[v.cliente].append(v)
    ventas_por_cliente = ventas_por_cliente.items()

    # Métricas
    total_ventas = ventas.count()
    ingresos_totales = ventas.aggregate(Sum('total'))['total__sum'] or 0
    productos_vendidos = ventas.aggregate(Sum('cantidad'))['cantidad__sum'] or 0

    # Crear / Editar / Eliminar en la misma vista
    if request.method == "POST":
        # CREAR
        if "crear" in request.POST:
            form = VentaForm(request.POST)
            if form.is_valid():
                venta = form.save(commit=False)
                producto = venta.producto
                # calcular total
                venta.total = producto.precio * venta.cantidad
                # validar stock
                if producto.stock >= venta.cantidad:
                    producto.stock -= venta.cantidad
                    producto.save()
                    venta.save()
                    messages.success(request, "✅ Venta registrada correctamente.")
                else:
                    messages.error(request, "⚠️ Stock insuficiente para registrar la venta.")
            else:
                messages.error(request, "⚠️ Error al registrar la venta. Revisa los campos.")

        # EDITAR (solo cliente y cantidad, mantiene el producto)
        elif "editar" in request.POST:
            venta = get_object_or_404(Venta, id=request.POST.get("id"))
            producto = venta.producto
            old_cant = venta.cantidad

            nuevo_cliente = request.POST.get("cliente", venta.cliente)
            try:
                nueva_cant = int(request.POST.get("cantidad", old_cant))
            except (TypeError, ValueError):
                messages.error(request, "⚠️ Cantidad inválida.")
                return redirect("ventas_list")

            # Ajuste de stock por diferencia
            delta = nueva_cant - old_cant
            if delta > 0:
                # necesita stock adicional
                if producto.stock < delta:
                    messages.error(request, "⚠️ Stock insuficiente para aumentar la cantidad.")
                    return redirect("ventas_list")
                producto.stock -= delta
            elif delta < 0:
                # se devuelve stock
                producto.stock += (-delta)

            # Guardar cambios
            producto.save()
            venta.cliente = nuevo_cliente
            venta.cantidad = nueva_cant
            venta.total = producto.precio * nueva_cant
            venta.save()
            messages.success(request, "✏️ Venta actualizada correctamente.")

        # ELIMINAR (opcional: reponer stock)
        elif "eliminar" in request.POST:
            venta = get_object_or_404(Venta, id=request.POST.get("id"))
            # si quieres reponer stock al eliminar, deja estas dos líneas:
            venta.producto.stock += venta.cantidad
            venta.producto.save()

            venta.delete()
            messages.success(request, "🗑️ Venta eliminada correctamente.")

        return redirect("ventas_list")

    context = {
        "ventas_por_cliente": ventas_por_cliente,
        "form": VentaForm(),  # para el modal de crear
        "total_ventas": total_ventas,
        "ingresos_totales": ingresos_totales,
        "productos_vendidos": productos_vendidos,
    }
    return render(request, "Ventas/ventas.html", context)
