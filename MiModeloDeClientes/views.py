from django.shortcuts import render, redirect

from .models import Producto, MetodoPago, Cliente
from .forms import *

def inicio (request):
    return render(request, 'MiModeloDeClientes/index.html')

def productos (request):
    if request.method == "POST":
        mi_formulario = ProductosFormulario(request.POST)
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            producto = Producto(nombre=informacion['nombre'], precio=informacion['precio'], descripcion=informacion['descripcion'])
            producto.save()
            return render (request, 'MiModeloDeClientes/index.html')
    else:
        mi_formulario = ProductosFormulario()
        return render(request, 'MiModeloDeClientes/productos.html', {"mi_formulario": mi_formulario})
    
def leer_productos(request):
    productos = Producto.objects.all()
    contexto = {"productos": productos}

    return render (request, "MiModeloDeClientes/leerProductos.html", contexto)


def clientes (request):
    if request.method == "POST":
        mi_formulario = ClientesFormulario(request.POST)
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            cliente = Cliente(nombre=informacion['nombre'], apellido=informacion['apellido'], email=informacion['email'])
            cliente.save()
            return render (request, 'MiModeloDeClientes/index.html')
    else:
        mi_formulario = ClientesFormulario()
        return render(request, 'MiModeloDeClientes/clientes.html', {"mi_formulario": mi_formulario})
    

def leer_clientes(request):
    clientes = Cliente.objects.all()
    contexto = {"clientes": clientes}

    return render(request, "MiModeloDeClientes/leerClientes.html", contexto)



def metodopago(request):
    if request.method == "POST":
        mi_formulario = MetodoDePagoFormulario(request.POST)
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            metodo = MetodoPago(nombre=informacion['nombre'])
            metodo.save()
            return render (request, 'MiModeloDeClientes/index.html')
    else:
        mi_formulario = MetodoDePagoFormulario()
        return render(request, 'MiModeloDeClientes/metododepago.html', {"mi_formulario":mi_formulario})
    

def leer_metodopago(request):
    metodos = MetodoPago.objects.all()
    contexto = {"metodos": metodos}

    return render (request, "MiModeloDeClientes/leerMetodos.html", contexto)

