from prestamos.models import Clientes

def datos_usuario(request):
    cliente_id = request.session.get("usuario_id") 
    
    if cliente_id: 
        try:
            cliente = Clientes.objects.get(id=cliente_id)
            return {"cliente": cliente}  
        except Clientes.DoesNotExist:
            return {}
    
    return {}