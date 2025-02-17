from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Clientes
from .forms import ClientesForm
from .forms import NuevoUsuarioForm
import string
import random
from django.core.mail import send_mail
# Create your views here.
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
        cliente.password = contraseña_generada  # Suponiendo que tienes un campo `contraseña` en el modelo
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



def login(request):
    return render(request, 'paginas/login.html')


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

def principal(request):
    return render(request, 'usuarios/principal.html')