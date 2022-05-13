from rest_framework import views
from rest_framework.response import Response
from authApp.serializers.clienteHabitualSerializer import ClienteHabitualSerializer

class ClienteHabitualCreateView(views.APIView):

    #Crea un cliente habitual en la BD 
    def post(self, request, *args, **kwargs): 

        serializer = ClienteHabitualSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()#guarda en la bd

        #Respuesta: codigo de respuesta CREADO
        return Response({"detail" : "Cliente habitual registrado exitosamente!!"})