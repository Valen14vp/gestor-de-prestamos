from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def inicio(request):
    return render(request, 'paginas/inicio.html')

def about(request):
    return HttpResponse("About")

def login(request):
    return render(request, 'paginas/login.html')
def clientes(request):
    return render(request, 'clientes/index.html')