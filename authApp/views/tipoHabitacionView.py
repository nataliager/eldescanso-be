from rest_framework.response import Response
from rest_framework.views import APIView
from authApp.models.tipo_habitacion import TipoHabitacion
from authApp.serializers.tipoHabitacionSerializer import TipoHabitacionSerializer
from rest_framework import generics

class TipoHabitacionView(APIView):

    #Obtiene todos los tipos de habitaciones de la BD
    def get(self, request, *args, **kwargs):

        tipohabitacion = TipoHabitacion.objects.all().order_by('tipo')
        serializer = TipoHabitacionSerializer(tipohabitacion,many=True)

        return Response(serializer.data)

        #GET FUNCIONA

#Vista concreta para recuperar, actualizar o eliminar una instancia de modelo
class DetailTipoHabitacionView(generics.RetrieveUpdateDestroyAPIView):

    queryset = TipoHabitacion.objects.all()
    serializer_class = TipoHabitacionSerializer

    #PATCH funciona correctamente
    #PUT funciona correctamente
    #GET funciona correctamente
    #DELETE funciona correctamente
