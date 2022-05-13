from django.db import models
from .servicio import Servicio
from .factura import Factura

class Servicio_incluido(models.Model):

    id = models.BigAutoField(primary_key=True, null=False, unique=True)#Numero entero grande serial-autoincrement
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE, null=False)
    factura = models.ForeignKey(Factura, on_delete=models.CASCADE, null=False)
    fecha_servicio = models.DateTimeField(unique=False, null=False)