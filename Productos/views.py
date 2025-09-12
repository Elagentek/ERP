from django.shortcuts import render, redirect
from .models import Producto
from .forms import ProductoForm

def productos_crud(request):
    productos = Producto.objects.all()

    # Calcular métricas
    total_productos = productos.count()
    stock_total = sum(p.stock for p in productos)
    valor_inventario = sum(p.precio * p.stock for p in productos)  # 👈 AQUÍ la multiplicación

    if request.method == "POST":
        if "crear" in request.POST:
            form = ProductoForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect("productos")
        elif "editar" in request.POST:
            producto = Producto.objects.get(id=request.POST["id"])
            form = ProductoForm(request.POST, instance=producto)
            if form.is_valid():
                form.save()
                return redirect("productos")
        elif "eliminar" in request.POST:
            producto = Producto.objects.get(id=request.POST["id"])
            producto.delete()
            return redirect("productos")
    else:
        form = ProductoForm()

    return render(request, "Productos/productos.html", {
        "productos": productos,
        "form": form,
        "total_productos": total_productos,
        "stock_total": stock_total,
        "valor_inventario": valor_inventario,  # 👈 lo mandamos al template
    })
