from django.db import models

# Create your models here.

tipo_producto =[
    [1, "Bien"],
    [2, "Servicio"]
]

class registrar(models.Model):
    codigo_principal = models.BigIntegerField(primary_key=True)
    codigo_auxiliar = models.BigIntegerField()
    tipo_producto = models.IntegerField(choices=tipo_producto)
    nombre = models.CharField(max_length=100)
    valor_unitario = models.FloatField()
    iva = models.IntegerField()
    ice = models.IntegerField()

    class Meta:
        verbose_name = 'registro'
        verbose_name_plural = 'registros'

    def __str__(self):
        return self.nombre