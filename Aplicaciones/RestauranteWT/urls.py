from django.urls import path
from . import views
app_name = 'RestauranteWT'
urlpatterns = [
    #URL INICIO
    path('', views.home),
    #URL PROVINCIAS 1
    path('listaProvincia/', views.listaProvincia),
    path('guardarProvincia/', views.guardarProvincia),
    path('eliminarProvincia/<int:id>', views.eliminarProvincia),
    path('editarProvincia/<int:id>/', views.editarProvincia),
    path('actualizarProvincia/', views.actualizarProvincia),
    #URL TIPOS DE COMIDA 2
    path('listaTipo/', views.listaTipo),
    path('guardarTipo/', views.guardarTipo),
    path('eliminarTipo/<int:id>', views.eliminarTipo),
    path('editarTipo/<int:id>', views.editarTipo),
    path('actualizarTipo/', views.actualizarTipo),
    #URL INGREDIENTES 3
    path('listaIngrediente/', views.listaIngrediente),
    path('guardarIngrediente/', views.guardarIngrediente),
    path('eliminarIngrediente/<int:id>', views.eliminarIngrediente),
    path('editarIngrediente/<int:id>', views.editarIngrediente),
    path('actualizarIngrediente/', views.actualizarIngrediente),
    #URL CLIENTES 4
    path('listaCliente/', views.listaCliente),
    path('guardarCliente/', views.guardarCliente),
    path('eliminarCliente/<int:id>', views.eliminarCliente),
    path('editarCliente/<int:id>', views.editarCliente),
    path('actualizarCliente/', views.actualizarCliente),
    #URL PEDIDOS 5
    path('listaPedido/', views.listaPedido),
    path('guardarPedido/', views.guardarPedido),
    path('eliminarPedido/<int:id>', views.eliminarPedido),
    path('editarPedido/<int:id>', views.editarPedido),
    path('actualizarPedido/', views.actualizarPedido),
    #URL PLATOS 6
    path('listaPlatillo/', views.listaPlatillo),
    path('guardarPlatillo/', views.guardarPlatillo),
    path('eliminarPlatillo/<int:id>', views.eliminarPlatillo),
    path('editarPlatillo/<int:id>', views.editarPlatillo),
    path('actualizarPlatillo/', views.actualizarPlatillo),
    #URL DETALLE 7
    path('listaDetalle/', views.listaDetalle),
    path('guardarDetalle/', views.guardarDetalle),
    path('eliminarDetalle/<int:id>', views.eliminarDetalle),
    path('editarDetalle/<int:id>', views.editarDetalle),
    path('actualizarDetalle/', views.actualizarDetalle),
    #URL RECETA 8
    path('listaReceta/', views.listaReceta),
    path('guardarReceta/', views.guardarReceta),
    path('eliminarReceta/<int:id>', views.eliminarReceta),
    path('editarReceta/<int:id>', views.editarReceta),
    path('actualizarReceta/', views.actualizarReceta),
]