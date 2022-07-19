from django.db import models

# Create your models here.

tipo_producto =[
    [1, "Bien"],
    [2, "Servicio"]
]

tipo_iva = [
    [1, '0%'],
    [2, '12%'],
    [3, '14%'],
    [4, 'No Objeto de Impuesto'],
    [5, 'Exento de IVA']
]

class Producto(models.Model):
    codigo_principal = models.BigIntegerField(primary_key=True)
    codigo_auxiliar = models.BigIntegerField()
    tipo_producto = models.IntegerField(choices=tipo_producto)
    nombre = models.CharField(max_length=100)
    valor_unitario = models.FloatField()
    iva = models.IntegerField(choices=tipo_iva)
    ice = models.IntegerField()

    class Meta:
        verbose_name = 'producto'
        verbose_name_plural = 'productos'

    def __str__(self):
        return self.nombre