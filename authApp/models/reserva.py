from django.db import models
from .cliente import Cliente
from .habitacion import Habitacion

class Reserva(models.Model):

    no_reserva = models.BigAutoField(primary_key=True)#Numero entero grande serial-autoincrement
    fecha_entrada = models.DateTimeField(null=False, unique=False)
    numero_dias = models.IntegerField(unique=False, null=False)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE,null=False)
    habitacion = models.ForeignKey(Habitacion, on_delete=models.CASCADE,null=False)





    