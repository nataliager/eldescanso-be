from rest_framework.response import Response
from rest_framework.views import APIView
from authApp.models.factura import Factura
from authApp.serializers.facturaSerializer import FacturaSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics

class FacturaView(APIView):

    permission_classes = [IsAuthenticated]

    #Obtiene todas las factura de la BD
    def get(self, request, *args, **kwargs):

        factura = Factura.objects.all()
        serializer = FacturaSerializer(factura,many=True)

        return Response(serializer.data)

        #GET FUNCIONA

#Vista concreta para recuperar, actualizar o eliminar una instancia de modelo
class DetailFacturaView(generics.RetrieveUpdateDestroyAPIView):

    permission_classes = [IsAuthenticated]

    queryset = Factura.objects.all()
    serializer_class = FacturaSerializer

    #PATCH funciona correctamente
    #PUT funciona correctamente
    #GET funciona correctamente
    #DELETE funciona correctamente