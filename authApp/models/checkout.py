from django.db import models
from .cliente import Cliente
from django.utils import timezone

class Checkout(models.Model):

    no_checkout = models.BigAutoField(primary_key=True)#Numero entero grande serial-autoincrement
    fecha_salida = models.DateTimeField(unique=False, null=False, default= timezone.now())
    cliente = models.ForeignKey(Cliente,  on_delete=models.CASCADE, null=False)