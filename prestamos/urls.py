from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('login/', views.login, name='login'),
    path('clientes/', views.clientes, name='clientes'),
    path('clientes/crear', views.crear_clientes, name='crear_clientes'),
    path('clientes/editar', views.editar_clientes, name='editar_clientes'),
    path('clientes/eliminar/<int:id>/', views.eliminar_clientes, name='eliminar_clientes'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
