from django.db import models

# Create your models here.    
class Usuarios(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, null=False, blank=False)
    email = models.CharField(max_length=100, null=False, blank=False)
    password = models.CharField(max_length=255, null=False, blank=False)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'usuarios'
        managed = True

class Clientes(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, null=False, blank=False)
    email = models.CharField(max_length=100, null=True, blank=True)
    telefono = models.CharField(max_length=25, null=True, blank=True)
    direccion = models.CharField(max_length=255, null=True, blank=True)
    identificacion = models.CharField(max_length=45, null=True, blank=True)
    calificacion = models.DecimalField(max_digits=2, decimal_places=1, default=0.0)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    activo = models.BooleanField(default=True)
    usuarios = models.ForeignKey(
        'Usuarios', 
        on_delete=models.CASCADE, 
        db_column='usuarios_id',
        default=0
    )

    class Meta:
        db_table = 'clientes'
        managed = True    
    

class Prestamos(models.Model):
    id = models.AutoField(primary_key=True)
    monto = models.DecimalField(max_digits=12, decimal_places=2, null=False, blank=False)
    tasa_intereses = models.DecimalField(max_digits=5, decimal_places=2, null=False, blank=False)
    plazo = models.IntegerField(null=False, blank=False)
    fecha_solicitud = models.DateTimeField(null=True, blank=True)
    estado = models.CharField(max_length=20, default="pendiente")
    clientes = models.ForeignKey(
        'Clientes', 
        on_delete=models.CASCADE, 
        db_column='clientes_id',
        default=0
        
    )

    class Meta:
        db_table = 'prestamos'
        managed = True


    
    
class Recibos_prestamos(models.Model):
    id = models.AutoField(primary_key=True)
    tipo_recibo = models.CharField(max_length=50, null=False, blank=False)
    imagen = models.ImageField(upload_to='imagenes/', null=True, blank=True)
    nombre_archivo = models.CharField(max_length=255, null=True, blank=True)
    fecha_subida = models.DateTimeField(auto_now_add=True)  # CURRENT_TIMESTAMP
    prestamos = models.ForeignKey(
        'Prestamos', 
        on_delete=models.CASCADE, 
        db_column='prestamos_id',
        related_name='recibos',
        default=0
    )

    class Meta:
        db_table = 'recibos'
        managed = True
