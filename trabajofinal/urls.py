from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('productos/listar/', views.listar_productos),
    path('', views.mostrar_producto),
    path('productos/agregar/<str:nombre>/<int:precio>/<int:stock_actual>/', views.agregar_producto),
    path('productos/actualizar/<int:id>/<str:nombre>/<int:precio>/<int:stock_actual>', views.update_producto_id),
    path('productos/borrar/<int:id>', views.borrar_producto_id),
    
    path('provedores/agregar/<str:nombre>/<str:apellido>/<int:dni>', views.agregar_proveedor),
    path('provedores/actualizar/<str:nombre>/<str:apellido>/<int:dni>', views.update_provedor_id),
    path('provedores/borrar/<str:nombre>/<str:apellido>/<int:dni>', views.borrar_provedor_id),
    path('provedores/listar/', views.listar_proveedor),
    path('provedores/mostrar/', views.mostrar_provedores)
]
