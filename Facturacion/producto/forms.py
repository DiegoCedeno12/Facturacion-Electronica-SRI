from django import forms
from .models import registrar

class ProductoForm(forms.ModelForm):

    class Meta:
        model = registrar
        #fields ["name", "email", "type_consult", "message", "notice"]
        fields = '__all__'