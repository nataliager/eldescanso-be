from rest_framework import views
from rest_framework.response import Response
from authApp.serializers.facturaSerializer import FacturaSerializer

class FacturaCreateView(views.APIView):

    #Crea una factura en la BD 
    def post(self, request, *args, **kwargs): 

        serializer = FacturaSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()#guarda en la bd

        #Respuesta: codigo de respuesta CREADO
        return Response({"detail" : "Factura generada exitosamente!!"})