from email import message
from multiprocessing import context
from django.shortcuts import redirect, render, HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from .forms import Contact, ContactForm

# Create your views here.
def home(request):
    return render(request, "core/home.html")

def contact(request):
    data = { 'form': ContactForm() }
    return render(request, "core/contact.html", data)

def autenticar(request):
    if request.method == 'POST':
        form = AuthenticationForm(data= request.POST)
        if form.is_valid():
            return redirect('home')
    else:
        form = AuthenticationForm()
    context = {'form': form}
    return render(request, "core/autenticar.html", {'form':form})

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