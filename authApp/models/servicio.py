from django.db import models

class Servicio(models.Model):

    cod_servicio = models.CharField(primary_key=True, max_length=50, unique=True, null=False)
    nombre = models.CharField(max_length=50, unique=False, null=False)
    precio = models.IntegerField(unique=False, null=False)
    



    