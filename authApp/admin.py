from django.contrib import admin
from .models.user import User
from .models.solicitud import Solicitud
from .models.servicio import Servicio
from .models.factura import Factura
from .models.servicio_incluido import Servicio_incluido
from .models.checkout import Checkout
from .models.reserva import Reserva
from .models.cliente import Cliente
from .models.clienteHabitual import ClienteHabitual
from .models.habitacion import Habitacion

# Register your models here.
admin.site.register(User)
admin.site.register(Solicitud)
admin.site.register(Servicio)
admin.site.register(Factura)
admin.site.register(Servicio_incluido)
admin.site.register(Checkout)
admin.site.register(Reserva)
admin.site.register(Cliente)
admin.site.register(ClienteHabitual)
admin.site.register(Habitacion)

