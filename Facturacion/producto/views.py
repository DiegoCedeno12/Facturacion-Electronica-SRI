from django.shortcuts import render
from .models import registrar
from .forms import ProductoForm

# Create your views here.

def registrarprod(request):
    data = { 'form': ProductoForm() }
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Registro Enviado"
        else:
            data["form"] = formulario
    return render(request, "producto/registrarprod.html")