from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from authApp.models.solicitud import Solicitud
from authApp.serializers.solicitudSerializer import SolicitudSerializer
from rest_framework import generics

class SolicitudView(APIView):

    permission_classes = [IsAuthenticated]

    #Obtiene todas las solicitudes de la BD
    def get(self, request, *args, **kwargs):

        solicitud = Solicitud.objects.all()
        serializer = SolicitudSerializer(solicitud,many=True)

        return Response(serializer.data)

        #GET FUNCIONA

#Vista concreta para recuperar, actualizar o eliminar una instancia de modelo
class DetailSolicitudView(generics.RetrieveUpdateDestroyAPIView):

    permission_classes = [IsAuthenticated]

    queryset = Solicitud.objects.all()
    serializer_class = SolicitudSerializer

    #PATCH funciona correctamente
    #PUT funciona correctamente
    #GET funciona correctamente
    #DELETE funciona correctamente