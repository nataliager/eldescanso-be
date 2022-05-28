from rest_framework import serializers
from authApp.models.reserva import Reserva
from authApp.models.cliente import Cliente
from authApp.models.habitacion import Habitacion
from authApp.models.tipo_habitacion import TipoHabitacion
from authApp.serializers import tipoHabitacionSerializer
from authApp.serializers.habitacionSerializer import HabitacionSerializer, HabitacionSerializerRepresentation
from authApp.serializers.clienteSerializer import ClienteSerializer
from authApp.serializers.tipoHabitacionSerializer import TipoHabitacionSerializer
from django.http.response import Http404

class ReservaSerializer(serializers.ModelSerializer):

    class Meta:

        model = Reserva
        fields = ['no_reserva', 'fecha_entrada', 'numero_dias',"cliente","habitacion"]  

        def to_representation(self, obj):  

            reserva = Reserva.objects.get(no_reserva=obj.no_reserva)
            cliente = Cliente.objects.get(no_identificacion=obj.no_identificacion)
            habitacion = Habitacion.objects.get(no_habitacion=obj.no_habitacion)
        
            return {
                'no_reserva': reserva.no_reserva,
                'fecha_entrada': reserva.fecha_entrada,
                'numero_dias': reserva.numero_dias,
                'cliente': cliente.no_identificacion,
                'habitacion': habitacion.no_habitacion,
                
            }

class ReservaSerializerRepresentation(serializers.ModelSerializer):
    
    cliente = ClienteSerializer() 
    habitacion = HabitacionSerializerRepresentation()
    #tipo = TipoHabitacionSerializer()

    class Meta:

        model = Reserva
        fields = ['no_reserva', 'fecha_entrada', 'numero_dias',"cliente","habitacion"]  

        def to_representation(self, obj):  

            reserva = Reserva.objects.get(no_reserva=obj.no_reserva)
            cliente = Cliente.objects.get(no_identificacion=obj.no_identificacion)
            habitacion = Habitacion.objects.get(no_habitacion=obj.no_habitacion)
        
            return {
                'no_reserva': reserva.no_reserva,
                'fecha_entrada': reserva.fecha_entrada,
                'numero_dias': reserva.numero_dias,
                'cliente': {
                    'no_identificacion': cliente.no_identificacion,
                    'nombre' : cliente.nombre,
                    'telefono': cliente.telefono,
                    'correo': cliente.correo
                },
                'habitacion': {
                    'no_habitacion': habitacion.no_habitacion,
                    'estado': habitacion.estado
                }   
            }

    #Valida si la reserva esta en la BD
    def get_object(pk):
        try:
            return Reserva.objects.get(pk=pk)
        except Reserva.DoesNotExist:
            raise Http404
