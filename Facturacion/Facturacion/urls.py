"""Facturacion URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import django
from django.contrib import admin
from django.urls import path
from django.urls import include
from core import views

urlpatterns = [
    path('', views.home, name='home'),
    path('registrarprod/', views.registrarprod, name='registrarprod'),
    path('contact/', views.contact, name='contact'),
    path('autent/', views.autent, name='autent'),
    path('registrar/', views.registrar, name='registrar'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
]
