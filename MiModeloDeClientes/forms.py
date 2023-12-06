from django import forms
from .models import *

class ClientesFormulario (forms.ModelForm):
    class Meta:
        model : Cliente
        fields: ['nombre', 'apellido', 'email'] 
    

class ProductosFormulario (forms.ModelForm):
    class Meta: 
        model: Producto
        fields: ['nombre', 'precio', 'descripcion']

class MetodoDePagoFormulario(forms.ModelForm):
    class Meta:
        model: MetodoPago
        fields: ['nombre']




