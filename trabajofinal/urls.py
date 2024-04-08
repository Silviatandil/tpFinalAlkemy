from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.mostrar_productos, name='mostrar_productos'),
    path('mostrar_proveedor/', views.mostrar_proveedor, name='mostrar_proveedor'),
    path('crear_proveedor/', views.crearProveedor, name='crear_proveedor'),
    path('crear_producto/',views.crearProducto, name='crear_producto'),
    path('filter/<int:StockActual>', views.filtrar_productos_stock),
    path('filter/<int:dni>',views.filtrar_proveedor_dni),
    path('update_producto_id/<int:id>/<str:nombre>/<int:precio>/<int:StockActual>', views.update_producto_id),
    path('update_proveedor_dni/<int:id>/<str:nombre>/<str:apellido>/<int:dni>', views.update_proveedor_id),
    path('borrarProducto_id/<int:id>', views.borrarProducto_id),
    path('borrarProveedor_id/<int:id>', views.borrarProveedor_id),
    path('delete',views.borrarProducto),
    path('delete/', views.borrarProveedor)
]