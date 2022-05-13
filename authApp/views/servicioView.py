from rest_framework.response import Response
from rest_framework.views import APIView
from authApp.models.servicio import Servicio
from authApp.serializers.servicioSerializer import ServicioSerializer
from rest_framework import generics

class ServicioView(APIView):

    #Obtiene todos los servicios de la BD
    def get(self, request, *args, **kwargs):

        servicio = Servicio.objects.all()
        serializer = ServicioSerializer(servicio,many=True)

        return Response(serializer.data)

        #GET FUNCIONA

#Vista concreta para recuperar, actualizar o eliminar una instancia de modelo
class DetailServicioView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Servicio.objects.all()
    serializer_class = ServicioSerializer

    #PATCH funciona correctamente
    #PUT funciona correctamente
    #GET funciona correctamente
    #DELETE funciona correctamente