from django.db import models

# Create your models here.    
class Usuarios(models.Model):
    id = models.AutoField(primary_key=True)
    nombre_usuario = models.CharField(max_length=100, null=False, blank=False , default="Nombre de usuario")
    nombre_empresa = models.CharField(max_length=100, null=False, blank=False, default="Nombre de la empresa")
    telefono = models.CharField(max_length=25, null=False, blank=False, default="+54 11 1234-5678")
    email = models.CharField(max_length=100, null=False, blank=False)
    password = models.CharField(max_length=255, null=False, blank=False)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'usuarios'
        managed = True

    def __str__(self):
        fila= "Nombre: " + self.nombre + " - Email: " + self.email
        return fila

class Clientes(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, null=False, blank=False, default="Nombre Apellido")
    email = models.CharField(max_length=100, null=False, blank=False, default="example@email.com")
    telefono = models.CharField(max_length=25, null=False, blank=False,default="+54 11 1234-5678")
    direccion = models.CharField(max_length=255, null=False, blank=False,default="direccion 12345")
    identificacion = models.CharField(max_length=45, null=False, blank=False,default="123456789")
    calificacion = models.DecimalField(max_digits=2, decimal_places=1, default=0.0)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    activo = models.BooleanField(default=True)
    usuario = models.ForeignKey(
        'Usuarios', 
        on_delete=models.CASCADE, 
        db_column='usuario_id',
        default=1
    )

    class Meta:
        db_table = 'clientes'
        managed = True    
    def __str__(self):
        fila= "Nombre: " + self.nombre + " - Email: " + self.email
        return fila

class Prestamos(models.Model):
    id = models.AutoField(primary_key=True)
    monto = models.DecimalField(max_digits=12, decimal_places=2, null=False, blank=False)
    tasa_intereses = models.DecimalField(max_digits=5, decimal_places=2, null=False, blank=False)
    plazo = models.IntegerField(null=False, blank=False)
    fecha_solicitud = models.DateTimeField(null=True, blank=True)
    estado = models.CharField(max_length=20, default="pendiente", null=False, blank=False)
    cliente = models.ForeignKey(
        'Clientes', 
        on_delete=models.CASCADE, 
        db_column='cliente_id',
        default=1
    )

    class Meta:
        db_table = 'prestamos'
        managed = True
    def __str__(self):
        return f"Prestamo ID: {self.id} - C Nombre: {self.cliente.nombre} - Monto: {self.monto}"


class Recibos_Prestamos(models.Model):
    id = models.AutoField(primary_key=True)
    tipo_recibo = models.CharField(max_length=50, null=False, blank=False)
    imagen = models.ImageField(upload_to='imagenes/', null=True, blank=True)
    nombre_archivo = models.CharField(max_length=255, null=True, blank=True)
    fecha_subida = models.DateTimeField(auto_now_add=True)
    prestamo = models.ForeignKey(
        'Prestamos', 
        on_delete=models.CASCADE, 
        db_column='prestamo_id',
        related_name='recibos',
        default=1
    )

    class Meta:
        db_table = 'recibos'
        managed = True
    def __str__(self):
        return f"Recibo ID: {self.id} - C Nombre: {self.prestamo.cliente.nombre}"
    def delete(self, using=None, keep_parents=False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()
    def clean(self):
        if not self.imagen:
            raise ValidationError("La imagen no puede estar vacía.")
        super().clean()