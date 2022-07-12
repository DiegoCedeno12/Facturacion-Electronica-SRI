from dataclasses import fields
from pyexpat import model
from django import forms
from django.urls import clear_script_prefix
from .models import Contact
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        #fields ["name", "email", "type_consult", "message", "notice"]
        fields = '__all__'

class UserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "password1", "password2"]

class AuthenticationForm(AuthenticationForm):

    class Meta:
        model = User
        fields = ["username", "password"]