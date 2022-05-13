from rest_framework import serializers
from authApp.models.user import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'rol', 'nombre','username', 'password', 'telefono']

    def create(self, validated_data):
        userInstance = User.objects.create(**validated_data)
        return userInstance

    def to_representation(self, obj):
            
        user = User.objects.get(id=obj.id)

        return {
            'id': user.id,
            'rol': user.rol,
            'nombre': user.nombre,
            'username': user.username,
            'telefono': user.telefono,
        }

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    pass