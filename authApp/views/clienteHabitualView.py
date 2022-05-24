from rest_framework.response import Response
from rest_framework.views import APIView
from authApp.models.clienteHabitual import ClienteHabitual
from authApp.serializers.clienteHabitualSerializer import ClienteHabitualSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics

class ClienteHabitualView(APIView):

    permission_classes = [IsAuthenticated]

    #Obtiene todos los clientes habituales de la BD
    def get(self, request, *args, **kwargs):

        clientehabitual = ClienteHabitual.objects.all()
        serializer = ClienteHabitualSerializer(clientehabitual,many=True)

        return Response(serializer.data)

        #GET FUNCIONA

#Vista concreta para recuperar, actualizar o eliminar una instancia de modelo
class DetailClienteHabitualView(generics.RetrieveUpdateDestroyAPIView):

    permission_classes = [IsAuthenticated]

    queryset = ClienteHabitual.objects.all()
    serializer_class = ClienteHabitualSerializer

    #PATCH funciona correctamente
    #PUT funciona correctamente
    #GET funciona correctamente
    #DELETE funciona correctamente

#Obtiene el descuento de un cliente habitual por su no_identificacion
class ClienteHabitualFilter(APIView):

    def get(self, request, *args, **kwargs):
        
        clientehabitual = ClienteHabitual.objects.filter(no_identificacion=request.query_params.get('no_identificacion')).distinct()
        tmp = []
        for u in clientehabitual:
            tmp.append(ClienteHabitualSerializer(u).data.get('descuento'))
        return Response({
            'descuento': tmp
        })