from django.urls import path
from tienda import views
from tienda.views import VerImagenes, EjemploLocalStorage , buscarpedido, buscarpedido2, para_ajax
from tienda import views_agregar


urlpatterns = [
    #Aca cargamos los pedidos
    path('cargar/', views.cargar_imagen, name='cargar'),
    #aca vamos a ver un pedido en particular.
    path('<int:pedido_id>', views.ver_imagen, name='ver'),
    #La ruta para la clase que nos va a mostrar las eimagenes
    path('verimagenes/', VerImagenes.as_view(), name='verimagenes'),
    #La ruta para la clase de localstorage
    path('localstorage/', EjemploLocalStorage.as_view(), name='localstorage'),
    #La ruta para la clase de localstorage
    #Esta pagina va a recibir informacion
    path('agregar/', views_agregar.agregar, name='agregar'),
    #Esta pagina va a trabajar con AJAX
    path('usar_ajax/', views.para_ajax, name='usar_ajax'),
    path('buscar_pedido/', buscarpedido.as_view(), name='buscar_pedido'),
    path('buscar_pedido2/', buscarpedido2.as_view(), name='buscar_pedido2'),
    


]
