from django.urls import path
from . import views

urlpatterns = [
    path('inicio/', views.inicio, name='inicio'),
    path('about/', views.about),
    path('login/', views.login, name='login'),
    path('clientes/', views.clientes, name='clientes'),
]
