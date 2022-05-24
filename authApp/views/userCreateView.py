from rest_framework import status, views
from rest_framework.response import Response
from authApp.serializers.userSerializer import UserSerializer


class UserCreateView(views.APIView):

   
    def post(self, request, *args, **kwargs): #solo metodo post

        serializer = UserSerializer(data=request.data)#creacion obj UserSerializer-> json q llega
        serializer.is_valid(raise_exception=True)#verificar si la info esta correcta
        serializer.save()#guarda en la bd

        #Respuesta valor del token y un codigo de respuesta
        return Response({"detail" : "Usuario registrado con exito!!."},status=status.HTTP_201_CREATED) 

   