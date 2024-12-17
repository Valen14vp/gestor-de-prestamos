from django.contrib import admin

# Register your models here.
from .models import Usuarios
admin.site.register(Usuarios)
from .models import Clientes
admin.site.register(Clientes)
from .models import Prestamos
admin.site.register(Prestamos)
from .models import Recibos_Prestamos
admin.site.register(Recibos_Prestamos)
