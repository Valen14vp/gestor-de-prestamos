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