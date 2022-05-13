from rest_framework import views
from rest_framework.response import Response
from authApp.serializers.clienteSerializer import ClienteSerializer

class ClienteCreateView(views.APIView):

    #Crea un cliente en la BD 
    def post(self, request, *args, **kwargs): 

        serializer = ClienteSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()#guarda en la bd

        #Respuesta: codigo de respuesta CREADO
        return Response({"detail" : "Cliente registrado exitosamente!!"})