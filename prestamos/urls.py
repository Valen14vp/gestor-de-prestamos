from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello),
    path('about/', views.about),
    path('login/', views.login),
]