from django.db import models
from django.utils import timezone
from .checkout import Checkout
from .reserva import Reserva

class Factura(models.Model):


    no_factura = models.BigAutoField(primary_key=True)#Numero entero grande serial-autoincrement
    fecha_factura = models.DateTimeField(null=False, default= timezone.now())
    precio_total = models.IntegerField(unique=False, null=False)
    reserva = models.ForeignKey(Reserva, on_delete=models.CASCADE,null=False)
    checkout = models.ForeignKey(Checkout, on_delete=models.CASCADE,null=False)
    