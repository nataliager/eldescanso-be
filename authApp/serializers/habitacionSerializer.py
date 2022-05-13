from rest_framework import serializers
from authApp.models.habitacion import Habitacion
from authApp.models.tipo_habitacion import TipoHabitacion

class HabitacionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Habitacion
        fields = ['no_habitacion','tipo','estado']  

        def to_representation(self, obj):  
            
            habitacion = Habitacion.objects.get(no_habitacion=obj.no_habitacion)
            tipohabitacion = TipoHabitacion.objects.get(tipohabitacion=obj.tipo)

            return {
                'no_habitacion': habitacion.no_habitacion,
                'tipo': tipohabitacion.tipo,
                'estado': habitacion.estado,
            }