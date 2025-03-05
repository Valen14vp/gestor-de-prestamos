from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('registro/', views.nuevo_usuario, name='registro'),
    path('login/', views.login, name='login'),
    path('clientes/', views.clientes, name='clientes'),
    path('clientes/crear', views.crear_clientes, name='crear_clientes'),
    path('clientes/editar/<int:id>/', views.editar_clientes, name='editar_clientes'),
    path('clientes/eliminar/<int:id>/', views.eliminar_clientes, name='eliminar_clientes'),
    path('principal/', views.principal, name='principal'),
    path("logout/", views.logout_usuario, name="logout"),
    path("ayuda/", views.ayuda, name="ayuda"),
    path("historial/", views.historial, name="historial"),
    path("calendario/", views.calendario, name="calendario"),
    path("estadisticas/", views.estadisticas, name="estadisticas"),
    path("solicitar/", views.solicitar_prestamo, name="solicitar"),
    path("ajuste/", views.ajustes, name="ajustes"),
    path("menu_opciones/", views.menu_opciones, name="menu_opciones"),
    path("prestamos/", views.prestamos_soli, name="prestamos"),
    path("prestamos/revision/<int:id>/", views.ver_prestamo, name="ver_prestamo"),
    path('prestamos/cambiar_estado/<int:id>/<str:accion>/', views.cambiar_estado_prestamo, name='cambiar_estado_prestamo'),
    

    
    
    
    
    
    
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
