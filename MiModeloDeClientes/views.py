from django.shortcuts import render, redirect
from .models import Producto, MetodoPago, Cliente
from .forms import *

def inicio (request):
    return render(request, 'MiModeloDeClientes/index.html')

def clientes_list (request):
    clientes = Cliente.objects.all()
    return render (request, 'MiModeloDeClientes/clientes.html', {'clientes': clientes})

def productos_list (request):
    productos = Producto.objects.all()
    return render (request, 'MiModeloDeClientes/productos.html', {'productos': productos})

def metododepago_list (request):
    metodo = MetodoPago.objects.all()
    return render (request, 'MiModeloDeClientes/metododepago.html', {'metodo': metodo})

def agregar_producto(request):
    if request.method == "POST":
        form = ProductosFormulario(request.POST)
        if form.is_valid():
            producto = form.save()
            return redirect("MiModeloDeClientes:index")
        else: 
            form = ProductosFormulario()
        return render(request, 'productos.html', {'form':form})

def agregar_cliente(request):
    if request.method == "POST":
        form = ClientesFormulario(request.POST)
        if form.is_valid():
            cliente = form.save()
            return redirect("MiModeloDeClientes:index")
        else:
            form = ClientesFormulario()
            return render(request, 'clientes.html', {'form':form})
        

def agregar_metodopago(request):
    if request.method == "POST":
        form = MetodoDePagoFormulario(request.POST)
        if form.is_valid():
            metodo = form.save()
            return redirect("MiModeloDeClientes:index")
        else:
            form = MetodoDePagoFormulario()
            return render(request, 'metododepago.html', {'form':form})
        

