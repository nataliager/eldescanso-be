from rest_framework.response import Response
from rest_framework.views import APIView
from authApp.models.cliente import Cliente
from authApp.serializers.clienteSerializer import ClienteSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics

class ClienteView(APIView):

    permission_classes = [IsAuthenticated]

    #Obtiene todos los clientes de la BD
    def get(self, request, *args, **kwargs):

        cliente = Cliente.objects.all().order_by('nombre')
        serializer = ClienteSerializer(cliente,many=True)

        return Response(serializer.data)

        #GET FUNCIONA

#Vista concreta para recuperar, actualizar o eliminar una instancia de modelo
class DetailClienteView(generics.RetrieveUpdateDestroyAPIView):

    permission_classes = [IsAuthenticated]

    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

    #PATCH funciona correctamente
    #PUT funciona correctamente
    #GET funciona correctamente
    #DELETE funciona correctamente