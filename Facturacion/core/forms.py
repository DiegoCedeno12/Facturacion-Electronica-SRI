from email.mime import audio
from pyexpat import model
from django.contrib.auth.models import User

class CustomUserForm(UserCreationForm):
    class meta:
        model = User
        