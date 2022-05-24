from rest_framework import  views
from rest_framework.response import Response
from authApp.serializers.solicitudSerializer import SolicitudSerializer

class SolicitudCreateView(views.APIView):

    #Crea una solicitud en la BD 
    def post(self, request, *args, **kwargs): #solo metodo post

        serializer = SolicitudSerializer(data=request.data)#creacion obj UserSerializer-> json q llega
        serializer.is_valid(raise_exception=True)#verificar si la info esta correcta
        serializer.save()#guarda en la bd

        #Respuesta: codigo de respuesta CREADO
        return Response({"detail" : "La solicitud fue enviada exitosamente, pronto un asesor se comunicara contigo."})