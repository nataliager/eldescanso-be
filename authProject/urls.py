from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from authApp import views
from authApp.views.login import Login

urlpatterns = [

    #URLs login
    #path('login/', TokenObtainPairView.as_view()),
    path('login/', Login.as_view()),
    path('refresh/', TokenRefreshView.as_view()),

    #URLs modelo User
    path('usercreate/', views.UserCreateView.as_view()),#crear un usuario
    path('userdetail/', views.UserDetailView.as_view()),#obtener todos los usuarios
    path('user/<str:pk>/', views.DetailUserView.as_view()),#crud usuario 
    path('user-view/', views.UserView.as_view()),#obtener y actualizar datos del usuario logueado

    #URLs modelo Solicitud
    path('solicitud/', views.SolicitudCreateView.as_view()),#crear una solicitud 
    path('solicitudes/', views.SolicitudView.as_view()),#obtener todas las solicitudes
    path('solicitud/<str:pk>/', views.DetailSolicitudView.as_view()),#crud solicitud

    #URLs modelo Servicio
    path('servicio/', views.ServicioCreateView.as_view()),#crear un servicio
    path('servicios/', views.ServicioView.as_view()),#obtener todos los servicios
    path('servicio/<str:pk>/', views.DetailServicioView.as_view()),#crud servicio

    #URLs modelo Habitacion
    path('habitacion/', views.HabitacionCreateView.as_view()),#crear una habitacion
    path('habitaciones/', views.HabitacionView.as_view()),#obtener todas las habitaciones
    path('habitacion/<int:pk>/', views.DetailHabitacionView.as_view()),#crud habitacion
    path('habitacionfilter/', views.HabitacionFilter.as_view()),#filtro habitacion por tipo
    path('habitacionestadofilter/', views.EstadoHabitacionFilter.as_view()),#filtro estado en que se encuentra la habitacion

    #URLs modelo TipoHabitacion
    path('tipohabitacion/', views.TipoHabitacionCreateView.as_view()),#crear una habitacion
    path('tipohabitaciones/', views.TipoHabitacionView.as_view()),#obtener todos los tipos de habitacion
    path('tipohabitacion/<str:pk>/', views.DetailTipoHabitacionView.as_view()),#crud tipo habitacion
    path('tipohabitacionfilter/', views.TipoHabitacionFilter.as_view()),#crud tipo habitacion

    #URLs modelo Checkout 
    path('checkout/', views.CheckoutCreateView.as_view()),#crear un checkout
    path('checkouts/', views.CheckoutView.as_view()),#obtener todos los checkouts
    path('checkout/<str:pk>/', views.DetailCheckoutView.as_view()),#crud checkout

    #URLs modelo Factura 
    path('factura/', views.FacturaCreateView.as_view()),#crear una factura
    path('facturas/', views.FacturaView.as_view()),#obtener todas las facturas
    path('factura/<str:pk>/', views.DetailFacturaView.as_view()),#crud factura

    #URLs modelo Servicio_incluido -- SIN PROBAR
    path('servicioincluido/', views.ServicioIncluidoCreateView.as_view()),#agregar un servicio incluido 
    path('serviciosincluidos/', views.ServicioIncluidoView.as_view()),#obtener todos los servicios incluidos
    path('servicioincluido/<int:pk>/', views.DetailServicioIncluidoView.as_view()),#crud servicio incluido

    #URLs modelo Cliente 
    path('cliente/', views.ClienteCreateView.as_view()),#crear un cliente
    path('clientes/', views.ClienteView.as_view()),#obtener todos los clientes
    path('cliente/<str:pk>/', views.DetailClienteView.as_view()),#crud cliente

    #URLs modelo Cliente_habitual 
    path('clientehabitual/', views.ClienteHabitualCreateView.as_view()),#crear un cliente habitual
    path('clienteshabituales/', views.ClienteHabitualView.as_view()),#obtener todos los clientes habituales
    path('clientehabitual/<int:pk>/', views.DetailClienteHabitualView.as_view()),#crud cliente habitual
    path('clientehabitualfilter/', views.ClienteHabitualFilter.as_view()),#crud cliente habitual

    #URLs modelo Reserva 
    path('reserva/', views.ReservaCreateView.as_view()),#registrar una reserva
    path('reservas/', views.ReservaView.as_view()),#obtener todas las reservas
    path('reserva/<str:pk>/', views.DetailReservaView.as_view()),#crud reserva

]
