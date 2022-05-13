from django.db import models
from .cliente import Cliente
from django.utils import timezone

class Checkout(models.Model):

    no_checkout = models.CharField(primary_key=True, max_length=10, unique=True, null=False)
    fecha_salida = models.DateTimeField(unique=False, null=False, default= timezone.now())
    cliente = models.ForeignKey(Cliente,  on_delete=models.CASCADE, null=False)