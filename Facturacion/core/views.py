from email import message
from multiprocessing import context
from django.shortcuts import redirect, render, HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from .forms import Contact, ContactForm
from producto.models import registrar
from producto.forms import ProductoForm

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

def contact(request):
    data = { 'form': ContactForm() }
    if request.method == 'POST':
        formulario = ContactForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Registro Enviado"
        else:
            data["form"] = formulario
    return render(request, "core/contact.html", data)


def autent(request):
    if request.method == 'POST':
        form = AuthenticationForm(data= request.POST)
        if form.is_valid():
            return redirect('home')
    else:
        form = AuthenticationForm()
    context = {'form': form}
    return render(request, "core/autent.html", {'form':form})


def registrar(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            message.success(request, f'usuario {username} creado')
    else:
        form = UserCreationForm()
    context = {'form': form}
    return render(request, "core/registrar.html", {'form':form})