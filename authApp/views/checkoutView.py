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

        checkout = Checkout.objects.all()
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