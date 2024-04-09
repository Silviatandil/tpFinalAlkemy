from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto, Proveedor
from .forms import ProveedorForm, ProductoForm  # Importa el formulario correspondiente

def crearProducto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mostrar_productos')  # Redirige a la lista de proveedores después de crear uno nuevo
    else:
        form = ProductoForm()
    return render(request, 'crear_producto.html', {'form': form})

def mostrar_productos(request):
    productos = Producto.objects.all()
    return render(request, 'lista_producto.html', {'productos': productos})

def filtrar_productos_stock(request):
    productoEncontrado = Producto.objects.filter(StockActual=2)
    print(productoEncontrado)
    return render(request, 'productoEncontrado.html', {'productoEncontrado': productoEncontrado})

def update_producto_id(request, id):
    producto = get_object_or_404(Producto, id=id)  # Obtiene el proveedor por su ID o muestra un error 404 si no existe
    
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('mostrar_productos')  # Redirige a la lista de proveedores después de actualizar uno
    else:
        form = ProductoForm(instance=producto)
    
    return render(request, 'update_producto.html', {'form': form, 'producto': producto})

def borrarProducto_id(request, id):
    productoBorrar = Producto.objects.get(id = id)
    productoBorrar.delete()
    productos = Producto.objects.all()
    return render(request, 'lista_producto.html', {'productos': productos})

def borrarProducto(request):
    productos = Producto.objects.all()
    productos.delete()
    return render(request, 'lista_producto.html', {'productos': productos})

def agregar_proveedor_formulario(request):
    return render(request, 'agregar_proveedor_formulario.html')

def crearProveedor(request):
    if request.method == 'POST':
        form = ProveedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mostrar_proveedor')  # Redirige a la lista de proveedores después de crear uno nuevo
    else:
        form = ProveedorForm()
    return render(request, 'crear_proveedor.html', {'form': form})

def mostrar_proveedor(request):
    proveedores = Proveedor.objects.all()
    return render(request, 'lista_proveedores.html', {'proveedores': proveedores} )

def filtrar_proveedor_dni(request):
    proveedorEncontrado = Proveedor.objects.filter(dni = 34562239)
    return render(request, 'proveedorEncontrado.html', {'proveedorEncontrado': proveedorEncontrado}) 



def update_proveedor_id(request, id):
    proveedor = get_object_or_404(Proveedor, id=id)  # Obtiene el proveedor por su ID o muestra un error 404 si no existe
    
    if request.method == 'POST':
        form = ProveedorForm(request.POST, instance=proveedor)
        if form.is_valid():
            form.save()
            return redirect('mostrar_proveedor')  # Redirige a la lista de proveedores después de actualizar uno
    else:
        form = ProveedorForm(instance=proveedor)
    
    return render(request, 'update_proveedor.html', {'form': form, 'proveedor': proveedor})


def borrarProveedor_id(request, id):
    proveedorBorrar = Proveedor.objects.get(id = id)
    proveedorBorrar.delete()
    proveedores = Proveedor.objects.all()
    return render(request, 'lista_proveedores.html', {'proveedores': proveedores} ) 


def borrarProveedor(request):
    proveedores = Proveedor.objects.all()
    proveedores.delete()
    return render(request, 'lista_proveedores.html', {'proveedores': proveedores} ) 
