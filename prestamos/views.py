from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def inicio(request):
    return render(request, 'paginas/inicio.html')


def login(request):
    return render(request, 'paginas/login.html')
def clientes(request):
    return render(request, 'clientes/index.html')

def crear_clientes(request):
    return render(request, 'clientes/crear.html')

def editar_clientes(request):
    return render(request, 'clientes/editar.html')