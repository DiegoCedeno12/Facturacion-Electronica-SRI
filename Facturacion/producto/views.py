from django.shortcuts import render
from .models import Producto
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

def listar_productos(request):
    productos = Producto.objects.all()
    
    data = {
        'Producto' : productos
    }

    return render(request, "producto/listar.html", data)