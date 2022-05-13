from rest_framework import views
from rest_framework.response import Response
from authApp.serializers.checkoutSerializer import CheckoutSerializer

class CheckoutCreateView(views.APIView):

    #Crea un checkout en la BD 
    def post(self, request, *args, **kwargs): 

        serializer = CheckoutSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()#guarda en la bd

        #Respuesta: codigo de respuesta CREADO
        return Response({"detail" : "Checkout registrado exitosamente!!"})