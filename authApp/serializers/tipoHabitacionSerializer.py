from rest_framework import serializers
from authApp.models.tipo_habitacion import TipoHabitacion

class TipoHabitacionSerializer(serializers.ModelSerializer):

    class Meta:
        model = TipoHabitacion
        fields = ['tipo', 'precio']  

    def to_representation(self, obj):  
        
        tipohabitacion = TipoHabitacion.objects.get(tipo=obj.tipo)

        return {

            'tipo': tipohabitacion.tipo,
            'precio': tipohabitacion.precio
        }