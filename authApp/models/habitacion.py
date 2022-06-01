from django.db import models
from authApp.models.tipo_habitacion import TipoHabitacion

class Habitacion(models.Model):

    no_habitacion = models.IntegerField(primary_key=True,unique=True, null=False)
    tipo = models.ForeignKey(TipoHabitacion, on_delete=models.CASCADE,null=False)
    estado = models.CharField( max_length=12,unique=False,null=False)






    