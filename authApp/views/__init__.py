#User
from .userCreateView import UserCreateView
from .userView import UserView
from .userDetailView import UserDetailView
from .userView import DetailUserView
from .userView import InformeMensual
from .userView import InformeMensualServicios

#Solicitud
from .solicitudCreateView import SolicitudCreateView
from .solicitudView import SolicitudView
from .solicitudView import DetailSolicitudView
from .solicitudView import SolicitudFilter

#Servicio
from .servicioCreateView import ServicioCreateView
from .servicioView import  ServicioView
from .servicioView import  DetailServicioView

#Habitación
from .habitacionCreateView import HabitacionCreateView
from .habitacionView import HabitacionView
from .habitacionView import DetailHabitacionView
from .habitacionView import HabitacionFilter
from .habitacionView import PrecioHabitacionFilter
from .habitacionView import OcupacionHotel

#Tipo habitación
from .tipoHabitacionCreateView import TipoHabitacionCreateView
from .tipoHabitacionView import TipoHabitacionView
from .tipoHabitacionView import DetailTipoHabitacionView

#Checkout
from .checkoutCreateView import CheckoutCreateView
from .checkoutView import CheckoutView
from .checkoutView import DetailCheckoutView
from .checkoutView import CheckoutCliente

#Factura
from .facturaCreateView import FacturaCreateView
from .facturaView import FacturaView
from .facturaView import DetailFacturaView
from .facturaView import PorcentajeCancelacion


#Servicio_incluido
from .servicioIncluidoCreateView import ServicioIncluidoCreateView
from .servicioIncluidoView import ServicioIncluidoView
from .servicioIncluidoView import DetailServicioIncluidoView
from .servicioIncluidoView import ServiciosFactura

#Cliente
from .clienteCreateView import ClienteCreateView
from .clienteView import ClienteView
from .clienteView import DetailClienteView

#Cliente_habitual
from .clienteHabitualCreateView import ClienteHabitualCreateView
from .clienteHabitualView import ClienteHabitualView
from .clienteHabitualView import DetailClienteHabitualView
from .clienteHabitualView import ClienteHabitualFilter

#Reserva
from .reservaCreateView import ReservaCreateView
from .reservaView import ReservaView
from .reservaView import DetailReservaView
from .reservaView import ReservasCliente

#Login
from .login import Login

