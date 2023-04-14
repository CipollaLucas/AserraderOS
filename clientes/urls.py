from django.urls import path
from pedidos import views
#from clientes import views_login
from clientes import views_logout
#from clientes import views_registro
from clientes.views_login import ListadoUsuario, RegistroUsuario, pagina_login
from django.contrib.auth.decorators import login_required
#from clientes import views_perfil


urlpatterns = [
    path("", views.home, name="home"),
    path("login", pagina_login, name="login"),
    path("logout", views_logout.pagina_logout, name="logout"),
    path("registro", RegistroUsuario.as_view(), name="registro"),
    path("lista_usuarios", login_required(ListadoUsuario.as_view()), name="lista_usuarios"),
]
