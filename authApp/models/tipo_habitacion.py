from django.db import models

class TipoHabitacion(models.Model):

    tipo = models.CharField(primary_key=True,max_length=50, unique=False, null=False)
    descripcion = models.TextField(max_length=500,unique=False, null=False)
    precio = models.IntegerField(unique=False, null=False)




    