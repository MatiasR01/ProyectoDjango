from django.urls import path
from . import views


app_name = "ABM"
urlpatterns = [
    path('', views.index, name="index"),
    path('busqueda/', views.buscar, name="busqueda"),
    path('agregar', views.agregar, name="agregar"),
    path('editar/<int:producto_id>', views.editar, name="editar"),
    path('acerca', views.acerca, name="acerca"),
    path('eliminar/<int:producto_id>', views.eliminar, name="eliminar"),
    path('productosver/<int:producto_id>', views.productosver, name="productosver"),
    path('categorias/<str:producto_categoria>', views.categoriasFiltro, name="categorias"),

]