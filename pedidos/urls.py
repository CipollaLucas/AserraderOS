# URLS.PY sirve para definir las diferentes rutas asociadas a las vistas

from django.urls import path
from pedidos import views
from tienda.views  import VerImagenes

urlpatterns = [
    path("", views.home, name="home"),
    path("productos/", views.productos, name="productos"),
    path("servicios/", views.servicios, name="servicios"),
    path("pedidos/", VerImagenes.as_view(), name="verimagenes"),
    path("about/", views.about, name="about"),
]
