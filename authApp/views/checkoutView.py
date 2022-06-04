from rest_framework.response import Response
from rest_framework.views import APIView
from authApp.models.checkout import Checkout
from authApp.serializers.checkoutSerializer import CheckoutSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics

class CheckoutView(APIView):

    permission_classes = [IsAuthenticated]

    #Obtiene todas los checkouts de la BD
    def get(self, request, *args, **kwargs):

        checkout = Checkout.objects.all().order_by('fecha_salida')
        serializer = CheckoutSerializer(checkout,many=True)

        return Response(serializer.data)

        #GET FUNCIONA

#Vista concreta para recuperar, actualizar o eliminar una instancia de modelo
class DetailCheckoutView(generics.RetrieveUpdateDestroyAPIView):

    permission_classes = [IsAuthenticated]

    queryset = Checkout.objects.all()
    serializer_class = CheckoutSerializer

    #PATCH funciona correctamente
    #PUT funciona correctamente
    #GET funciona correctamente
    #DELETE funciona correctamente

#Obtener datos de un checkout por cliente
class CheckoutCliente(APIView):

    permission_classes = [IsAuthenticated]

    #metodo GET funciona correctamente
    def get(self, request, *args, **kwargs):
        
        checkouts =  Checkout.objects.filter(cliente=request.query_params.get('cliente')).distinct().order_by('fecha_salida')
        tmp = []
        for u in checkouts:
            tmp.append(CheckoutSerializer(u).data)
        return Response(tmp)