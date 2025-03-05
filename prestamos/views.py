from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password, make_password
from .models import Clientes, Prestamos
from .forms import ClientesForm, NuevoUsuarioForm, SolicitarPrestamoForm
from django.http import JsonResponse
import string
import random


#inicio-------------------------------------------------------------------------------------------------------------

def inicio(request):
    return render(request, 'paginas/inicio.html')

def nuevo_usuario(request):
    formulario= NuevoUsuarioForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        cliente = formulario.save(commit=False)

            # Generar una contraseña aleatoria
        longitud = 10
        caracteres = string.ascii_letters + string.digits
        contraseña_generada = ''.join(random.choice(caracteres) for _ in range(longitud))

            # Guardar la contraseña generada en el cliente
        cliente.password = make_password(contraseña_generada)  
        cliente.save()
        
        send_mail(
                'Bienvenido a Préstamo Click',
                f'Hola {cliente.nombre}, tu registro fue exitoso. Tu contraseña es: {contraseña_generada}',
                'prestamoclick25@gmail.com',  # Correo del remitente
                [cliente.email],  # Correo del destinatario
                fail_silently=False,
            )
        return redirect('inicio')
    else:
        formulario = NuevoUsuarioForm()
    return render(request, 'paginas/nuevo_usuario.html', {'formulario': formulario})




#clientes-------------------------------------------------------------------------------------------------------------

def menu_opciones(request):
    return render(request, 'clientes/menu_de_opciones.html')



def clientes(request):
    filtro = request.GET.get('filtro', 'todos') 
    if filtro == 'activos':
        clientes = Clientes.objects.filter(activo=True)
    elif filtro == 'inactivos':
        clientes = Clientes.objects.filter(activo=False)
    else:
        clientes = Clientes.objects.all()

    return render(request, 'clientes/index.html', {'clientes': clientes, 'filtro_actual': filtro})




def crear_clientes(request):
    formulario = ClientesForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return  redirect('clientes')
    return render(request, 'clientes/crear.html', {'formulario': formulario})

def editar_clientes(request, id):
    cliente = Clientes.objects.get(id=id)
    formulario = ClientesForm(request.POST or None, request.FILES or None, instance=cliente)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('clientes')
    return render(request, 'clientes/editar.html', {'formulario': formulario})




def eliminar_clientes(request, id):
    cliente = Clientes.objects.get( id=id)  
    cliente.activo = 0                     
    cliente.save()                               
    return redirect('clientes') 



def prestamos_soli(request):
    filtro = request.GET.get('filtro', 'todos') 
    if filtro == 'activos':
        prestamos = Prestamos.objects.filter(estado="aprobado")
    elif filtro == 'inactivos':
        prestamos = Prestamos.objects.filter(estado="pendiente")
    else:
        prestamos = Prestamos.objects.all()

    return render(request, 'clientes/prestamos_solicitudes.html', {'prestamos': prestamos, 'filtro_actual': filtro})
    
    
    

def ver_prestamo(request, id):
    prestamo = Prestamos.objects.get(id=id)
    cliente = prestamo.cliente
    return render(request, 'clientes/revision.html', {'prestamo': prestamo, 'cliente': cliente})















#usuarios----------------------------------------------------------------------------------------------
def principal(request):
    cliente_id = request.session.get("cliente_id") 
    if not cliente_id:
        return redirect("login") 

    cliente = Clientes.objects.get(id=cliente_id)
    return render(request, "usuarios/principal.html", {"cliente": cliente})


def login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        try:
            cliente = Clientes.objects.get(email=email)

            if check_password(password, cliente.password):
                request.session["cliente_id"] = cliente.id 
                request.session.set_expiry(0) 
                
                return redirect("principal")

            else:
                messages.error(request, "Contraseña incorrecta.")

        except Clientes.DoesNotExist:
            messages.error(request, "Usuario no encontrado.")

    return render(request, "paginas/login.html")




def solicitar_prestamo(request):
    cliente_id = request.session.get("cliente_id")  
    if not cliente_id:
        return redirect("login") 

    cliente = Clientes.objects.get(id=cliente_id) 

    if request.method == "POST":
        formulario = SolicitarPrestamoForm(request.POST, request.FILES) 
        if formulario.is_valid():  
            prestamo = formulario.save(commit=False)
            prestamo.cliente = cliente  
            prestamo.save()  
            
            send_mail(
                'Solicitud de Préstamo NeonBank',
                f'Hola, {cliente.nombre} ha solicitado un préstamo por un monto de {prestamo.monto} pesos.',
                'prestamoclick25@gmail.com',  
                ['valen125125@gmail.com'],  
                fail_silently=False,
            )
            return redirect("principal")  
    else:
        formulario = SolicitarPrestamoForm() 

    return render(request, "usuarios/solicitar_prestamo.html", {"formulario": formulario, "cliente": cliente}) 
    




def ajustes(request):
    return render(request, "usuarios/ajustes.html")




def ayuda(request):
    return render(request, 'usuarios/ayuda.html')




def calendario(request):
    return render(request, 'usuarios/calendario.html')




def historial(request):
    return render(request, 'usuarios/historial.html')




def estadisticas(request):
    return render(request, 'usuarios/estadisticas.html')



def logout_usuario(request):
    request.session.flush() 
    return redirect("login")















