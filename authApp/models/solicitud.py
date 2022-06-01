from django.db import models

class Solicitud(models.Model):

    id = models.BigAutoField(primary_key=True)#Numero entero grande serial-autoincrement
    email = models.EmailField(max_length=50, null=False)
    nombre = models.CharField(max_length=50, unique=False, null=False)
    telefono = models.CharField(max_length=15, unique=False, null=False)
    estado = models.CharField(max_length=45, unique=False, null=False, default="pendiente")
    





