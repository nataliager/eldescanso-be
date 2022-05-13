from rest_framework import serializers
from authApp.models.clienteHabitual import ClienteHabitual
from authApp.models.cliente import Cliente

class ClienteHabitualSerializer(serializers.ModelSerializer):

    class Meta:
        model = ClienteHabitual
        fields = ['id', 'no_identificacion', 'tipo_cliente', 'descuento']  

        def to_representation(self, obj):  
            
        
            clientehabitual = ClienteHabitual.objects.get(id=obj.id)
            cliente = Cliente.objects.get(no_identificacion=obj.no_identificacion)

            return {
                'id':  clientehabitual.id,
                'no_identificacion': cliente.no_identificacion,
                'tipo_cliente': clientehabitual.tipo_cliente,
                'descuento': clientehabitual.descuento,
            }