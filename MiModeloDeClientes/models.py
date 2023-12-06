from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=20)
    precio = models.DecimalField(decimal_places=2, max_digits=10)
    descripcion = models.CharField(max_length=100)

class Cliente(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    


class MetodoPago (models.Model):
    nombre = models.CharField(max_length=30)
    

    

