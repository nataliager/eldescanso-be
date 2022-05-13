from rest_framework import serializers
from authApp.models.checkout import Checkout
from authApp.models.cliente import Cliente

class CheckoutSerializer(serializers.ModelSerializer):

    class Meta:
        model = Checkout
        fields = ['no_checkout', 'fecha_salida', 'cliente']  

        def to_representation(self, obj):  

            checkout = Checkout.objects.get(id=obj.id)
            cliente = Cliente.objects.get(no_identificacion=obj.no_identificacion)
        
            return {
                'no_checkout': checkout.no_checkout,
                'fecha_salida': checkout.fecha_salida,
                'cliente': cliente.no_identificacion
            }
