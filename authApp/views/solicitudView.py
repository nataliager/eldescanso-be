from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from authApp.models.solicitud import Solicitud
from authApp.serializers.solicitudSerializer import SolicitudSerializer
from rest_framework import generics

class SolicitudView(APIView):

    #Obtiene todas las solicitudes de la BD
    def get(self, request, *args, **kwargs):

        solicitud = Solicitud.objects.all()
        serializer = SolicitudSerializer(solicitud,many=True)

        return Response(serializer.data)

        #GET FUNCIONA

#Vista concreta para recuperar, actualizar o eliminar una instancia de modelo
class DetailSolicitudView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Solicitud.objects.all()
    serializer_class = SolicitudSerializer

    #PATCH funciona correctamente
    #PUT funciona correctamente
    #GET funciona correctamente
    #DELETE funciona correctamente

#Obtener listado de habitaciones disponibles
class SolicitudFilter(APIView):

    permission_classes = [IsAuthenticated]

    #metodo GET funciona correctamente
    def get(self, request, *args, **kwargs):
        
        solicitudes = Solicitud.objects.filter(estado=request.query_params.get('estado')).distinct()
        tmp = []
        for u in solicitudes:
            if SolicitudSerializer(u).data.get('estado') == "pendiente":
                tmp.append(SolicitudSerializer(u).data)
        return Response({
            'solicitudes': tmp
        })