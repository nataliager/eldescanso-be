from rest_framework.response import Response
from rest_framework.views import APIView
from authApp.models.servicio_incluido import Servicio_incluido
from authApp.serializers.servicioIncluidoSerializer import ServicioIncluidoSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics

class ServicioIncluidoView(APIView):

    permission_classes = [IsAuthenticated]

    #Obtiene todos los servicio incluidos en factura de la BD
    def get(self, request, *args, **kwargs):

        servicioincluido = Servicio_incluido.objects.all().order_by('fecha_servicio')
        serializer = ServicioIncluidoSerializer(servicioincluido,many=True)

        return Response(serializer.data)

        #GET FUNCIONA

#Vista concreta para recuperar, actualizar o eliminar una instancia de modelo
class DetailServicioIncluidoView(generics.RetrieveUpdateDestroyAPIView):
    
    permission_classes = [IsAuthenticated]

    queryset = Servicio_incluido.objects.all()
    serializer_class = ServicioIncluidoSerializer

    #PATCH funciona correctamente
    #PUT funciona correctamente
    #GET funciona correctamente
    #DELETE funciona correctamente

#Servicios incluidos a una factura
class ServiciosFactura(APIView):

    permission_classes = [IsAuthenticated]
  
    #metodo GET funciona correctamente
    def get(self, request, *args, **kwargs):
        
        servicios =  Servicio_incluido.objects.filter(factura=request.query_params.get('factura')).distinct().order_by('fecha_servicio')
        tmp = []
        for u in servicios:
            tmp.append(ServicioIncluidoSerializer(u).data)
        return Response(tmp)