from rest_framework import serializers
from authApp.models.checkout import Checkout
from authApp.models.factura import Factura
from authApp.models.reserva import Reserva

class FacturaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Factura
        fields = ['no_factura', 'fecha_factura', 'precio_total','reserva', 'checkout']  

        def to_representation(self, obj): 

            factura = Factura.objects.get(no_factura=obj.no_factura)
            reserva = Reserva.objects.get(no_reserva=obj.no_reserva) # busco obj reserva --> selected
            checkout = Checkout.objects.get(no_checkout=obj.no_checkout)

            return {
                'no_factura': factura.no_factura,
                'fecha_factura': factura.fecha_factura,
                'precio_total':  factura.precio_total,
                'reserva': reserva.no_reserva,
                'checkout': checkout.no_checkout,
            }

 

