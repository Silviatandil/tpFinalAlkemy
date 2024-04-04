from django.db import models


class Producto(models.Model):
    nombre = models.CharField(max_length = 100)
    precio = models.FloatField()
    stock_actual = models.IntegerField()
    def __str__(self):
        return self.nombre

 

class Proveedor(models.Model):
    nombre = models.CharField(max_length = 100)
    apellido = models.CharField(max_length = 100)
    dni = models.IntegerField()
    def __str__(self):
        return self.nombre


  























