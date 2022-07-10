import email
from django.db import models


# Create your models here.


options_consult = [
    [0, "Consulta"],
    [1, "Reclamo"],
    [2, "Sugerencia"],
    [3, "Felicidades"]
]

class Contact(models.Model):
    name = models.CharField(max_length=50, verbose_name="Nombre")
    email = models.EmailField(verbose_name="Correo Electronico")
    type_consult = models.IntegerField(choices=options_consult, verbose_name="Tipo de Consulta")
    message = models.TextField(verbose_name="Mensaje")
    notice = models.BooleanField(verbose_name="Aviso")

    class Meta:
        verbose_name = 'contacto'
        verbose_name_plural = 'contactos'

    def __str__(self):
        return self.name

    
