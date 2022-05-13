from django.db import models
from .cliente import Cliente
from .habitacion import Habitacion

class Reserva(models.Model):

    no_reserva = models.CharField(primary_key=True, max_length=10, unique=True, null=False)
    fecha_entrada = models.DateTimeField(null=False, unique=False)
    numero_dias = models.IntegerField(unique=False, null=False)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE,null=False)
    habitacion = models.ForeignKey(Habitacion, on_delete=models.CASCADE,null=False)