from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .forms import Contact, ContactForm, UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import Http404
from producto.forms import ProductoForm
from django.contrib import auth
from producto.views import Producto

# Create your views here.
def home(request):
    return render(request, "core/home.html")

def registrarprod(request):
    data = { 'form': ProductoForm() }
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Registro Enviado"
        else:
            data["form"] = formulario
    return render(request, "producto/registrarprod.html", data)

def listar_productos(request):
    productos = Producto.objects.all()
    
    data = {
        'productos' : productos
    }

    return render(request, "producto/listar.html", data)

def modificar(request, codigo_principal):
    productos = get_object_or_404(Producto, codigo_principal=codigo_principal)
    
    data = {
        'form' : ProductoForm(instance=productos)
    }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=productos)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="listar_productos")
        data["form"] = formulario

    return render(request, "producto/modificar.html", data)

def eliminar(request, codigo_principal):
    productos = get_object_or_404(Producto, codigo_principal=codigo_principal)
    productos.delete()
    return redirect(to="listar_productos")


def contact(request):
    data = { 'form': ContactForm() }
    if request.method == 'POST':
        formulario = ContactForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Registro Enviado')
        else:
            data["form"] = formulario
    return render(request, "core/contact.html", data)


@csrf_exempt
def autent(request):
    data = {
        'form': AuthenticationForm()
    }
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = auth.authenticate(username = form.cleaned_data["username"], password =form.cleaned_data["password"])
            auth.login(request, user)
            return redirect(to="home") 
        data["form"] = form

    return render(request, 'core/autent.html', data)

@csrf_exempt
def registrar(request):
    data = {
        'form': UserCreationForm()
    }
    
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            user = auth.authenticate(username = form.cleaned_data["username"], password =form.cleaned_data["password1"])
            auth.login(request, user)
            messages.success(request, "Te has registrado con exito")
            return redirect(to="home") 
        data["form"] = form
    return render(request, "core/registrar.html", data)

