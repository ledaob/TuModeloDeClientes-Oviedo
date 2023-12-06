from django.contrib import admin
from .models import *

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'apellido', 'email']
    list_filter = ['nombre', 'email']
    search_fields = ['nombre', 'apellido']


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'precio', 'descripcion']
    list_filter = ['nombre', 'precio']
    search_fields = ['nombre', 'precio']

@admin.register(MetodoPago)
class MetodoPagoAdmin(admin.ModelAdmin):
    list_display=['nombre']
    list_filter=['nombre']
    search_fields=['nombre']
    