from django import forms
from .models import Prestamos
from .models import Clientes
from .models import Recibos_Prestamos
from .models import Usuarios

class ClientesForm(forms.ModelForm):
    class Meta:
        model = Clientes
        fields = ['nombre', 'email', 'telefono', 'direccion', 'identificacion','activo']
        
class NuevoUsuarioForm(forms.ModelForm):
    class Meta:
        model = Clientes
        fields = ['nombre', 'email', 'telefono', 'direccion', 'identificacion']
        
class SolicitarPrestamoForm(forms.ModelForm):
    class Meta:
        model = Prestamos
        fields = ['monto', 'tasa_intereses', 'plazo', 'ingresos_mensuales', 'empleo_actual', 'imagen_recibo', 'imagen_dnifrente', 'imagen_dnireverso', 'terminos_y_condiciones']