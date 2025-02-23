from prestamos.models import Clientes

def datos_usuario(request):
    cliente_id = request.session.get("usuario_id")  # Aquí usas "cliente_id" en lugar de "clientes_id"
    
    if cliente_id:  # Debe coincidir con el nombre de la variable
        try:
            cliente = Clientes.objects.get(id=cliente_id)
            return {"cliente": cliente}  # Agregar datos al contexto global
        except Clientes.DoesNotExist:
            return {}
    
    return {}