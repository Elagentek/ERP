from django import forms
from .models import Venta

class VentaForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = ["cliente", "producto", "cantidad", "tipo", "fecha_entrega", "direccion"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["fecha_entrega"].widget.attrs.update({"type": "date"})
        self.fields["direccion"].widget.attrs.update({"placeholder": "Ej: Calle 123, Ciudad"})
