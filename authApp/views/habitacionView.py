from rest_framework.response import Response
from rest_framework.views import APIView
from authApp.models.habitacion import Habitacion
from authApp.serializers.habitacionSerializer import HabitacionSerializerRepresentation
from rest_framework import generics

class HabitacionView(APIView):

    #Obtiene todas las habitaciones de la BD
    def get(self, request, *args, **kwargs):

        habitacion = Habitacion.objects.all()
        serializer = HabitacionSerializerRepresentation(habitacion,many=True)

        return Response(serializer.data)

#Vista concreta para recuperar, actualizar o eliminar una instancia de modelo
class DetailHabitacionView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Habitacion.objects.all()
    serializer_class = HabitacionSerializerRepresentation

    #PATCH funciona correctamente
    #PUT funciona correctamente
    #GET funciona correctamente
    #DELETE funciona correctamente

#Obtener listado de habitaciones disponibles
class HabitacionFilter(APIView):

    #metodo GET funciona correctamente
    def get(self, request, *args, **kwargs):
        
        habitaciones = Habitacion.objects.filter(tipo=request.query_params.get('tipo')).distinct()
        tmp = []
        for u in habitaciones:
            if HabitacionSerializerRepresentation(u).data.get('estado') == "Disponible":
                tmp.append(HabitacionSerializerRepresentation(u).data)
        return Response({
            'habitaciones': tmp
        })

#Filtro precio habitacion segun su tipo por numero de habitacion
class PrecioHabitacionFilter(APIView):
    
    def get(self, request, *args, **kwargs):
        
        habitacion = Habitacion.objects.filter(no_habitacion=request.query_params.get('no_habitacion')).distinct()
        tmp = []
        for u in habitacion:
            tmp.append(HabitacionSerializerRepresentation(u).data.get('tipo'))
        return Response(tmp)



