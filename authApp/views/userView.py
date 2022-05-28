from rest_framework import status, views, generics
from django.conf import settings
from rest_framework.response import Response
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

#Serializadores
from authApp.serializers.userSerializer import UserSerializer
from authApp.serializers.facturaSerializer import InformeFacturaSerializer
from authApp.serializers.servicioIncluidoSerializer import ServicioIncluidoSerializer

#Modelos
from authApp.models.user import User
from authApp.models.factura import Factura
from authApp.models.servicio_incluido import Servicio_incluido


class UserView(views.APIView):

    permission_classes = (IsAuthenticated,)

    # Permite al usuario logueado ver sus datos
    def get(self, request, *args, **kwargs):

        token = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = tokenBackend.decode(token, verify=False)

        serializer = UserSerializer()
        u = User(id=valid_data["user_id"])
        result = serializer.to_representation(u)

        return Response(result, status=status.HTTP_200_OK)

    # Permite actualizar los datos de un usuario logueado
    def put(self, request, *args, **kwargs):

        # Decodificacion del token
        token = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = tokenBackend.decode(token, verify=False)

        request.data["id"] = valid_data["user_id"]  # obtener id del token
        user = User(id=valid_data["user_id"])  # crear un obj de tipo user

        # Actualizar el usuario autenticado
        serializer = UserSerializer(user, data=request.data)
        serializer.is_valid(raise_exception=True)  # valida
        updatedUser = serializer.save()  # guarda
        result = serializer.to_representation(updatedUser)  # convierte a json

        return Response(result, status=status.HTTP_200_OK)

    # Permite eliminar el usuario logueado
    def delete(self, request, *args, **kwargs):

        token = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = tokenBackend.decode(token, verify=False)

        request.data["id"] = valid_data["user_id"]  # obtener id del token
        u = User(id=valid_data["user_id"])  # crear un obj de tipo user
        u.delete()

        return Response({"detail": "El usuario fue eliminado exitosamente"}, status=status.HTTP_204_NO_CONTENT)

# Vista concreta para recuperar, actualizar o eliminar una instancia de modelo
class DetailUserView(generics.RetrieveUpdateDestroyAPIView):

    permission_classes = [IsAuthenticated]

    queryset = User.objects.all()
    serializer_class = UserSerializer

    # PATCH funciona correctamente
    # PUT funciona correctamente
    # GET funciona correctamente
    # DELETE funciona correctamente

#Clase que retorna un informe mensual de las ventas en el hotel el descanso
class InformeMensual(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):

        facturas = Factura.objects.filter(fecha_factura__contains=request.query_params.get(
            'fecha_factura')).order_by('fecha_factura')

        def dicti_result() -> dict:
            dicti = {}  
            for i in facturas:
                fecha = InformeFacturaSerializer(i).data.get('fecha_factura')
                precio = InformeFacturaSerializer(i).data.get('precio_total')
                fecha_filtro = fecha[0:str(fecha).find('T')]
                if fecha_filtro in dicti.keys():
                    dicti[fecha_filtro].append(str(precio))
                else:
                    dicti[fecha_filtro] = []
                    dicti[fecha_filtro].append(str(precio))

            resultado_total_dia = [{i: str(sum([float(j) for j in dicti[i]])) for i in dicti}]
            totalVentas = sum([float(resultado_total_dia[0][n]) for n in resultado_total_dia[0]])
            
            return {
                'Ventas': resultado_total_dia,
                'total_ventas': totalVentas
            }
        return Response(dicti_result())

#Clase que retorna un informe de ventas de los servicios en el hotel el descanso
class InformeMensualServicios(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):

        servicios = Servicio_incluido.objects.filter(fecha_servicio__contains=request.query_params.get(
            'fecha_servicio')).order_by('fecha_servicio')

        def dicti_result() -> dict:
            dicti = {}
            
            for i in servicios:

                servicio = ServicioIncluidoSerializer(i).data.get('servicio')

                if servicio in dicti.keys():
                    dicti[servicio].append(int(1))   
                else:
                    dicti[servicio] = []
                    dicti[servicio].append(int(1))
           
            resultado_servicios = [{i: int(sum([int(j) for j in dicti[i]])) for i in dicti}]
            totalVentas = sum([int(resultado_servicios[0][n]) for n in resultado_servicios[0]])

            return {
                'ventas_servicio': resultado_servicios[0],
                'total_ventas':totalVentas,
            }
        return Response(dicti_result())