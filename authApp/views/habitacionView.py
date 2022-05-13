from urllib import request
from rest_framework.response import Response
from rest_framework.views import APIView
from authApp.models.habitacion import Habitacion
from authApp.serializers.habitacionSerializer import HabitacionSerializer
from rest_framework import generics

class HabitacionView(APIView):

    #Obtiene todas las habitaciones de la BD
    def get(self, request, *args, **kwargs):

        habitacion = Habitacion.objects.all()
        serializer = HabitacionSerializer(habitacion,many=True)

        return Response(serializer.data)

        #GET FUNCIONA
        #FALTA FILTRAR POR ESTADO Y TIPO

#Vista concreta para recuperar, actualizar o eliminar una instancia de modelo
class DetailHabitacionView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Habitacion.objects.all()
    serializer_class = HabitacionSerializer

    #PATCH funciona correctamente
    #PUT funciona correctamente
    #GET funciona correctamente
    #DELETE funciona correctamente

#Vista concreta para recuperar, actualizar o eliminar una instancia de modelo
class HabitacionFilter(APIView):

    #Metodo para obtener info de un usuario (filtro)
    #metodo GET funciona correctamente
    def get(self, request, *args, **kwargs):
        
        habitaciones = Habitacion.objects.filter(tipo=request.query_params.get('tipo')).distinct()
        tmp = []
        for u in habitaciones:
            tmp.append(HabitacionSerializer(u).data)
        return Response({
            'habitaciones': tmp
        })


class EstadoHabitacionFilter(APIView):

    def get(self, request, *args, **kwargs):
        
        estado = Habitacion.objects.filter(no_habitacion=request.query_params.get('no_habitacion')).distinct()
        tmp = []
        for u in estado:
            tmp.append(HabitacionSerializer(u).data.get('estado'))
        return Response({
            'estado': tmp
        })



