from django.shortcuts import render
from .models import Producto, Proveedor

def agregar_producto(request,nombre, precio, stock_actual):
    producto_nuevo = Producto.objects.create(
        nombre = nombre,
        precio =precio,
        stock_actual = stock_actual
    )
    return render(request, 'nuevo_producto.html', {'producto_nuevo': producto_nuevo})

def listar_productos(request):
    productos = Producto.objects.all()
    return render(request, 'lista_productos.html', {'productos': productos})

def agregar_proveedor(request,nombre, apellido, dni):
    provedor_nuevo = Proveedor.objects.create(
        nombre = nombre,
        apellido = apellido,
        dni = dni
    )
    return render(request, 'provedor_nuevo.html', {'provedor_nuevo': provedor_nuevo})

def mostrar_producto(request):
   productos = Producto.objects.all()
   return render(request, 'lista_productos.html', {'productos': productos})

def mostrar_provedores(request):
    provedores = Proveedor.objects.all()
    return render(request,'lista_provedores.html', {'provedores': provedores})

def update_producto_id(request, id, nombre,precio,stock_actual):
    productoActualizar = Producto.objects.get(id = id)
    productoActualizar.nombre = nombre
    productoActualizar.precio = precio
    productoActualizar.stock_actual = stock_actual
    productoActualizar.save()
    productos = Producto.objects.all()
    return render(request, 'lista_productos.html', {'productos': productos})

def update_provedor_id(request, id, nombre, apellido, dni):
    provedorActualizar = Proveedor.objects.get(id = id)
    provedorActualizar.nombre = nombre
    provedorActualizar.apellido = apellido
    provedorActualizar.dni = dni
    provedorActualizar.save()
    provedor = Proveedor.objects.all()

    return render(request, 'lista_provedores.html', {'provedor': provedor})

def borrar_producto_id(request, id):
    productoBorrar = Producto.objects.get(id = id)
    productoBorrar.delete()
    producto = Producto.objects.all()
    return render(request, 'lista_productos.html', {'productos': producto})

def borrar_provedor_id(request, id):
    provedorBorrar = Proveedor.objects.get(id = id)
    provedorBorrar.delete()
    provedor = Proveedor.objects.all()
    return render(request, 'lista_provedores.html', {'provedor': provedor})

def listar_proveedor(request):
       provedores = Proveedor.objects.all()
       return render(request, 'lista_provedores.html', {'provedores': provedores})
