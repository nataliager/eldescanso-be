from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from authApp.models.tipo_habitacion import TipoHabitacion
from authApp.serializers.tipoHabitacionSerializer import TipoHabitacionSerializer
from rest_framework import generics

class TipoHabitacionView(APIView):

    permission_classes = [IsAuthenticated]

    #Obtiene todos los tipos de habitaciones de la BD
    def get(self, request, *args, **kwargs):

        tipohabitacion = TipoHabitacion.objects.all()
        serializer = TipoHabitacionSerializer(tipohabitacion,many=True)

        return Response(serializer.data)

        #GET FUNCIONA

#Vista concreta para recuperar, actualizar o eliminar una instancia de modelo
class DetailTipoHabitacionView(generics.RetrieveUpdateDestroyAPIView):

    permission_classes = [IsAuthenticated]

    queryset = TipoHabitacion.objects.all()
    serializer_class = TipoHabitacionSerializer

    #PATCH funciona correctamente
    #PUT funciona correctamente
    #GET funciona correctamente
    #DELETE funciona correctamente

#Filtro de tipo de habitación 
class TipoHabitacionFilter(APIView):

    #Metodo para obtener precio de una habitacion por su tipo (filtro)
    #metodo GET funciona correctamente
    def get(self, request, *args, **kwargs):
        
        tipos = TipoHabitacion.objects.filter(tipo=request.query_params.get('tipo')).distinct()
        tmp = []

        for u in tipos:
            tmp.append(TipoHabitacionSerializer(u).data)
        return Response({
            'tipos': tmp
        })