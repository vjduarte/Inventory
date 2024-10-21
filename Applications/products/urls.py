import views
from django.urls import path

from . import views
app_name = 'products-app'
urlpatterns = [
    path('listarProductos/', views.ProductsListView.as_view(), name='listarProductos'),
    path('listaProdCategoria/',views.ProductsbyCategory.as_view(),name='listarPCategoria'),
    path('ver-productos/<pk>/',views.ProductsView.as_view(),name='verProductos'),
    path('agregarProducto/',views.ProductCreate.as_view(),name='agregarProducto'),
    path('actualizar-productos/<pk>/',views.ProductUpdate.as_view(),name='ActualizarProductos'),
    path('eliminar-productos/<pk>/',views.ProductDelete.as_view(),name='EliminarProductos'),


]