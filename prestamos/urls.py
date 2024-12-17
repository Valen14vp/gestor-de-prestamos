from django.urls import path
from . import views

urlpatterns = [
    path('inicio/', views.inicio, name='inicio'),
    path('about/', views.about),
    path('login/', views.login, name='login'),
    path('clientes/', views.clientes, name='clientes'),
    path('clientes/crear', views.crear_clientes, name='crear_clientes'),
    path('clientes/editar', views.editar_clientes, name='editar_clientes'),
]
