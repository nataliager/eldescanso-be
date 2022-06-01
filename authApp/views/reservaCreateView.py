from rest_framework import views
from rest_framework.response import Response
from authApp.serializers.reservaSerializer import ReservaSerializer
from rest_framework.permissions import IsAuthenticated

class ReservaCreateView(views.APIView):

    permission_classes = (IsAuthenticated,)

    #Crea una reserva en la BD 
    def post(self, request, *args, **kwargs): 

        serializer = ReservaSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()#guarda en la bd

        #Respuesta: codigo de respuesta CREADO
        return Response(serializer.data)