from rest_framework import serializers
from authApp.models import habitacion
from authApp.models.reserva import Reserva
from authApp.models.cliente import Cliente
from authApp.models.habitacion import Habitacion
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
                'habitacion': habitacion.no_habitacion
            }

    #Valida si la reserva esta en la BD
    def get_object(pk):
        try:
            return Reserva.objects.get(pk=pk)
        except Reserva.DoesNotExist:
            raise Http404
