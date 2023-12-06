from django.contrib import admin
from django.urls import path
from MiModeloDeClientes import views




urlpatterns = [
    path('clientes/', views.clientes_list, name="clientes"),
    path('productos/', views.productos_list, name= "productos"),
    path('metodoDePago/', views.metododepago_list, name="metododepago"),
    path('index/', views.inicio, name="inicio"),
    path('clientes/agregar/', views.agregar_cliente, name="agregar_cliente"),
    path('productos/agregar/', views.agregar_producto, name='agregar_producto'),
    path('metododepago/agregar/', views.agregar_metodopago, name='agregar_metodo'),

        
    
]