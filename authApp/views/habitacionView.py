from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from authApp.models.habitacion import Habitacion
from authApp.models.reserva import Reserva
from authApp.serializers.habitacionSerializer import HabitacionSerializerRepresentation
from authApp.serializers.reservaSerializer import ReservaSerializer, ReservaSerializerRepresentation
from rest_framework import generics

class HabitacionView(APIView):

    permission_classes = [IsAuthenticated]

    #Obtiene todas las habitaciones de la BD
    def get(self, request, *args, **kwargs):

        habitacion = Habitacion.objects.all().order_by('no_habitacion')
        serializer = HabitacionSerializerRepresentation(habitacion,many=True)

        return Response(serializer.data)

#Vista concreta para recuperar, actualizar o eliminar una instancia de modelo
class DetailHabitacionView(generics.RetrieveUpdateDestroyAPIView):

    permission_classes = [IsAuthenticated]

    queryset = Habitacion.objects.all()
    serializer_class = HabitacionSerializerRepresentation

    #PATCH funciona correctamente
    #PUT funciona correctamente
    #GET funciona correctamente
    #DELETE funciona correctamente

#Obtener listado de habitaciones disponibles
class HabitacionFilter(APIView):

    permission_classes = [IsAuthenticated]

    #metodo GET funciona correctamente
    def get(self, request, *args, **kwargs):
        
        habitaciones = Habitacion.objects.filter(tipo=request.query_params.get('tipo')).distinct()
        tmp = []
        for u in habitaciones:
            if HabitacionSerializerRepresentation(u).data.get('estado') == "disponible":
                tmp.append(HabitacionSerializerRepresentation(u).data)
        return Response({
            'habitaciones': tmp
        })

#Filtro precio habitacion segun su tipo por numero de habitacion
class PrecioHabitacionFilter(APIView):

    permission_classes = [IsAuthenticated]
    
    def get(self, request, *args, **kwargs):
        
        habitacion = Habitacion.objects.filter(no_habitacion=request.query_params.get('no_habitacion')).distinct().order_by('no_habitacion')
        tmp = []
        for u in habitacion:
            tmp.append(HabitacionSerializerRepresentation(u).data.get('tipo'))
        return Response(tmp)

#Obtener listado de habitaciones ocupadas
class OcupacionHotel(APIView):

    permission_classes = [IsAuthenticated]

    #metodo GET funciona correctamente
    def get(self, request, *args, **kwargs):
        
        reservas = Reserva.objects.filter(fecha_entrada__contains=request.query_params.get(
            'fecha_entrada')).order_by('fecha_entrada')

        habitaciones = Habitacion.objects.all().order_by('no_habitacion').distinct().order_by('no_habitacion')

        total_habitaciones_hotel = 0

        for i in habitaciones:
            total_habitaciones = HabitacionSerializerRepresentation(i).data
            total_habitaciones_hotel += 1   
            
            
    
        dicti = {} 
        contOcupada = 0

        for i in reservas:
            fecha = ReservaSerializer(i).data.get('fecha_entrada')
            #hab = ReservaSerializer(i).data.get('habitacion')
            habitacion = ReservaSerializerRepresentation(i).data.get('habitacion')
            
            #print(habitacion['estado'])
            #print(habitacion['no_habitacion'])
            fecha_filtro = fecha[0:str(fecha).find('T')]
            if fecha_filtro in dicti.keys():
                if str(habitacion['estado']) == "ocupada":
                    dicti[fecha_filtro].append(int(1))
            elif str(habitacion['estado']) == "ocupada":
                dicti[fecha_filtro] = []
                dicti[fecha_filtro].append(int(1))
            
            resultado_habitaciones = [{i: int(sum([int(j) for j in dicti[i]])) for i in dicti}]
            #resultado_habitaciones = [{i: int(len(dicti[i])/total_habitaciones) for i in dicti}]

        print(dicti.values())

        calculo = (contOcupada/total_habitaciones_hotel) * 1
        perCan = float("{0:.4f}".format(calculo))
        #print(dicti)
                            
        
        return Response({
            'dicti': resultado_habitaciones,
            'porcentaje_ocupacion' : perCan,
            'total_habitaciones': total_habitaciones_hotel,
        })