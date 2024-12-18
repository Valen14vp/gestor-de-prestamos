from django import forms
from .models import Prestamos
from .models import Clientes
from .models import Recibos_Prestamos
from .models import Usuarios

class ClientesForm(forms.ModelForm):
    class Meta:
        model = Clientes
        fields = ['nombre', 'email', 'telefono', 'direccion', 'identificacion','activo']