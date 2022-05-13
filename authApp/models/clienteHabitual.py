from django.db import models
from .cliente import Cliente

class ClienteHabitual(models.Model):

    id = models.BigAutoField(primary_key=True)#Numero entero grande serial-autoincrement
    no_identificacion = models.ForeignKey(Cliente, on_delete=models.CASCADE,null=False)
    tipo_cliente = models.CharField(max_length=12, unique=False, null=False)
    descuento = models.IntegerField(unique=False, null=True)