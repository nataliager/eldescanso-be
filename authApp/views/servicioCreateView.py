from rest_framework import views
from rest_framework.response import Response
from authApp.serializers.servicioSerializer import ServicioSerializer

class ServicioCreateView(views.APIView):

    #Crea un servicio en la BD 
    def post(self, request, *args, **kwargs):

        serializer = ServicioSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()#guarda en la bd

        #Respuesta: codigo de respuesta CREADO
        return Response({"detail" : "Servicio creado exitosamente!!"})