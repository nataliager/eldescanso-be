from rest_framework import views
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from authApp.serializers.servicioIncluidoSerializer import ServicioIncluidoSerializer

class ServicioIncluidoCreateView(views.APIView):

    permission_classes = [IsAuthenticated]

    #Crea una tabla de servicios incluidos en factura en la BD 
    def post(self, request, *args, **kwargs): 

        serializer = ServicioIncluidoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()#guarda en la bd

        #Respuesta: codigo de respuesta CREADO
        return Response({"detail" : "Servicio incluido exitosamente!!"})