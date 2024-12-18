from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Clientes
from .forms import ClientesForm
# Create your views here.
def inicio(request):
    return render(request, 'paginas/inicio.html')


def login(request):
    return render(request, 'paginas/login.html')
def clientes(request):
    clientes = Clientes.objects.all()
    return render(request, 'clientes/index.html', {'clientes': clientes})

def crear_clientes(request):
    formulario = ClientesForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return  redirect('clientes')
    return render(request, 'clientes/crear.html', {'formulario': formulario})

def editar_clientes(request):
    return render(request, 'clientes/editar.html')




def eliminar_clientes(request, id):
    cliente = Clientes.objects.get( id=id)  
    cliente.activo = 0                     
    cliente.save()                               
    return redirect('clientes') 