from django.contrib import admin
from django.urls import path
from MiModeloDeClientes import views




urlpatterns = [
    path('clientes/', views.clientes, name="clientes"),
    path('productos/', views.productos, name= "productos"),
    path('metodoDePago/', views.metodopago, name="metododepago"),
    path('index/', views.inicio, name="inicio"),   
    path('leerProductos/', views.leer_productos, name="leerProductos"),
    path('leerClientes/', views.leer_clientes, name="leerClientes"),
    path('leerMetodos/', views.leer_metodopago, name="leerMetodos"),

        
    
]