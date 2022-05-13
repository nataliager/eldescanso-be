from rest_framework_simplejwt.views import TokenObtainPairView
from authApp.serializers.userSerializer import CustomTokenObtainPairSerializer, UserSerializer
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework import status

class Login (TokenObtainPairView):

    serializer_class = CustomTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        username = request.data.get('username', '')
        password = request.data.get('password', '')
        user = authenticate(
            username=username,
            password=password
        )

        if user:
            login_serializer = self.serializer_class(data=request.data)
            if login_serializer.is_valid():
                user_serializer = UserSerializer(user)
                return Response({
                    'access': login_serializer.validated_data.get('access'),
                    'refresh': login_serializer.validated_data.get('refresh'),
                    'user': user_serializer.data,
                    'detail': 'Inicio de sesión Exitoso!'
                }, status=status.HTTP_200_OK)
            return Response({'Error': 'Credenciales incorrectas'},status=status.HTTP_400_BAD_REQUEST)
        return Response({'Error': 'Credenciales incorrectas'},status=status.HTTP_400_BAD_REQUEST)