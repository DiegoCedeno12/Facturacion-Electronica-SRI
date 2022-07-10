from dataclasses import fields
from pyexpat import model
from django import forms
from .models import Contact
from django.contrib.auth.models import User


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        #fields ["name", "email", "type_consult", "message", "notice"]
        fields = '__all__'