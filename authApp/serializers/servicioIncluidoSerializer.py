from rest_framework import serializers
from authApp.models.servicio_incluido import Servicio_incluido
from authApp.models.servicio import Servicio
from authApp.models.factura import Factura

class ServicioIncluidoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Servicio_incluido
        fields = ['id', 'servicio', 'factura', 'fecha_servicio']

    def to_representation(self, obj):

        servicioIncluido = Servicio_incluido.objects.get(id=obj.id)
        servicio = Servicio.objects.get(cod_servicio=obj.cod_servicio)
        factura = Factura.objects.get(no_factura=obj.no_factura)

        return {
            'id': servicioIncluido.id,
            'servicio': servicio.cod_servicio,
            'factura': factura.no_factura,
            'fecha_servicio': servicioIncluido.fecha_servicio,
        }
