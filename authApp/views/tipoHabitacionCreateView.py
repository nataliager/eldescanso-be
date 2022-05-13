from rest_framework import views
from rest_framework.response import Response
from authApp.serializers.tipoHabitacionSerializer import TipoHabitacionSerializer

class TipoHabitacionCreateView(views.APIView):

    #Crea un tipo de habitacion en la BD 
    def post(self, request, *args, **kwargs): 

        serializer = TipoHabitacionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()#guarda en la bd

        #Respuesta: codigo de respuesta CREADO
        return Response({"detail" : "Tipo de habitación agregado exitosamente!!"})