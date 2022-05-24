from rest_framework import serializers
from authApp.models.habitacion import Habitacion
from authApp.models.tipo_habitacion import TipoHabitacion
from authApp.serializers.tipoHabitacionSerializer import TipoHabitacionSerializer

class HabitacionSerializer(serializers.ModelSerializer):

    #tipo= TipoHabitacionSerializer() 

    class Meta:

        model = Habitacion
        fields = ['no_habitacion','tipo','estado'] 

        def to_representation(self, obj):  
                    
            habitacion = Habitacion.objects.get(no_habitacion=obj.no_habitacion)
            tipohabitacion = TipoHabitacion.objects.get(tipo=obj.tipo)

            return {
                'no_habitacion': habitacion.no_habitacion,
                'tipo': habitacion.tipo,
                'estado': habitacion.estado,
            }

class HabitacionSerializerRepresentation(serializers.ModelSerializer):

    tipo= TipoHabitacionSerializer() 

    class Meta:
    
        model = Habitacion
        fields = ['no_habitacion','tipo','estado'] 

        def to_representation(self, obj):  
                    
            habitacion = Habitacion.objects.get(no_habitacion=obj.no_habitacion)
            tipohabitacion = TipoHabitacion.objects.get(tipo=obj.tipo)

            return {
                'no_habitacion': habitacion.no_habitacion,
                'tipo': {
                    'tipo': tipohabitacion.tipo,
                    'caracteristicas': tipohabitacion.caracteristicas,
                    'precio': tipohabitacion.precio
                },
                'estado': habitacion.estado,
            }