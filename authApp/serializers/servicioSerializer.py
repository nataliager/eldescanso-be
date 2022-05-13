from rest_framework import serializers
from authApp.models.servicio import Servicio

class ServicioSerializer(serializers.ModelSerializer):

    class Meta: 
        model = Servicio
        fields = ['cod_servicio','nombre', 'precio'] 
    
    def to_representation(self, obj):
    
        servicio = Servicio.objects.get(cod_servicio=obj.cod_servicio)

        return {
            'cod_servicio': servicio.cod_servicio,
            'nombre': servicio.nombre,
            'precio': servicio.precio,
        }

