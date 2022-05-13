from rest_framework import views
from rest_framework.response import Response
from authApp.serializers.habitacionSerializer import HabitacionSerializer

class HabitacionCreateView(views.APIView):

    #Crea una habitacion en la BD 
    def post(self, request, *args, **kwargs): 

        serializer = HabitacionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()#guarda en la bd

        #Respuesta: codigo de respuesta CREADO
        return Response({"detail" : "La habitación fue creada exitosamente!!"})