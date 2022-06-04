from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from authApp.models.user import User
from authApp.serializers.userSerializer import UserSerializer

class UserDetailView(APIView):

    permission_classes = [IsAuthenticated]

    #Obtiene todos los usuarios de la BD
    def get(self, request, *args, **kwargs):

        users = User.objects.all().order_by('nombre')
        serializer = UserSerializer(users,many=True)

        return Response(serializer.data)

        #GET FUNCIONA