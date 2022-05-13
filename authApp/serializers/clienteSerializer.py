from rest_framework import serializers
from authApp.models.cliente import Cliente

class ClienteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cliente
        fields = ['no_identificacion', 'nombre', 'telefono', 'correo']  

    def to_representation(self, obj):  
        
        cliente = Cliente.objects.get(no_identificacion=obj.no_identificacion)

        return {
            'no_identificacion': cliente.no_identificacion,
            'nombre': cliente.nombre,
            'telefono': cliente.telefono,
            'correo': cliente.correo,
        }
