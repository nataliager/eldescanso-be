from django.db import models

class Cliente(models.Model):

    no_identificacion = models.CharField(primary_key=True, max_length=20, unique=True, null=False)
    nombre = models.CharField(max_length=50, unique=False, null=False)
    telefono = models.CharField(max_length=15, unique=False, null=False)
    correo = models.EmailField( max_length=50, null=False)