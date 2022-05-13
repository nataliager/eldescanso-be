from rest_framework import serializers
from authApp.models.solicitud import Solicitud

class SolicitudSerializer(serializers.ModelSerializer):

    class Meta: 
        model = Solicitud
        fields = ['id','email','nombre', 'telefono','estado']

    def to_representation(self, obj):

        solicitud = Solicitud.objects.get(id=obj.id)

        return {
            'id' : solicitud.id,
            'email': solicitud.email,
            'nombre': solicitud.nombre,
            'telefono': solicitud.telefono,
            'estado': solicitud.estado,
        }

