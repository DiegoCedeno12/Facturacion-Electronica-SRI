from pyexpat import model
from django import forms
from .models import Producto

class ProductoForm(forms.ModelForm):

    valor_unitario = forms.FloatField(min_value=0.1)

    class Meta:
        model = Producto
        #fields ["name", "email", "type_consult", "message", "notice"]
        fields = '__all__'