from logging import PercentStyle
from rest_framework.response import Response
from rest_framework.views import APIView
from authApp.models.factura import Factura
from authApp.models.reserva import Reserva
from authApp.serializers.facturaSerializer import FacturaSerializerRepresentation
from authApp.serializers.reservaSerializer import ReservaSerializerRepresentation
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics

class FacturaView(APIView):

    permission_classes = [IsAuthenticated]

    #Obtiene todas las factura de la BD
    def get(self, request, *args, **kwargs):

        factura = Factura.objects.all().order_by('no_factura')
        serializer = FacturaSerializerRepresentation(factura,many=True)

        return Response(serializer.data)

        #GET FUNCIONA

#Vista concreta para recuperar, actualizar o eliminar una instancia de modelo
class DetailFacturaView(generics.RetrieveUpdateDestroyAPIView):

    permission_classes = [IsAuthenticated]

    queryset = Factura.objects.all().order_by('no_factura')
    serializer_class = FacturaSerializerRepresentation

    #PATCH funciona correctamente
    #PUT funciona correctamente
    #GET funciona correctamente
    #DELETE funciona correctamente

#Obtener el porcentaje de cancelacion de reservas del hotel
class PorcentajeCancelacion(APIView):

    permission_classes = [IsAuthenticated]

    #metodo GET funciona correctamente
    def get(self, request, *args, **kwargs):
        
        facturas = Factura.objects.all().order_by('fecha_factura').distinct()
        contFact = 0
        
        reservas = Reserva.objects.all().order_by('fecha_entrada').distinct()
        contRes = 0

        for u in facturas:
              FacturaSerializerRepresentation(u).data
              contFact += 1

        for u in reservas:
            ReservaSerializerRepresentation(u).data
            contRes += 1

        calculo = (contFact / contRes) * 1
        perCan = float("{0:.4f}".format(calculo))
        
        
        return Response({
            'porcentaje_cancelacion': 1 - perCan
        })


