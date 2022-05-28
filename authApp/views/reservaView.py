from rest_framework.response import Response
from rest_framework.views import APIView
from authApp.models.reserva import Reserva
from authApp.serializers.reservaSerializer import ReservaSerializerRepresentation
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics

class ReservaView(APIView):

    permission_classes = [IsAuthenticated]

    #Obtiene todas las reservas de la BD
    def get(self, request, *args, **kwargs):

        reserva = Reserva.objects.all()
        serializer = ReservaSerializerRepresentation(reserva,many=True)

        return Response(serializer.data)

        #GET FUNCIONA

#Vista concreta para recuperar, actualizar o eliminar una instancia de modelo
class DetailReservaView(generics.RetrieveUpdateDestroyAPIView):

    permission_classes = [IsAuthenticated]

    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializerRepresentation

    #PATCH funciona correctamente
    #PUT funciona correctamente
    #GET funciona correctamente
    #DELETE funciona correctamente

#Obtener datos de una reserva por el cliente
class ReservasCliente(APIView):

    permission_classes = [IsAuthenticated]

    #metodo GET funciona correctamente
    def get(self, request, *args, **kwargs):
        
        reservas =  Reserva.objects.filter(cliente=request.query_params.get('cliente')).distinct()
        tmp = []
        for u in reservas:
            tmp.append(ReservaSerializerRepresentation(u).data)
        return Response(tmp)