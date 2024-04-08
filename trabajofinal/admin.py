from django.contrib import admin
from .models import Producto, Proveedor



class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'precio', 'stock_actual']
    search_fields = ['nombre', 'precio']
admin.site.register(Producto,ProductoAdmin)


class ProveedorAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'apellido', 'dni']
    search_fields = ['apellido', 'dni']
admin.site.register(Proveedor,ProveedorAdmin)
