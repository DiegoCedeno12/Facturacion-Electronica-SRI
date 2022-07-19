from django import forms
from .models import Producto

class ProductoForm(forms.ModelForm):

    class Meta:
        model = Producto
        #fields ["name", "email", "type_consult", "message", "notice"]
        fields = '__all__'