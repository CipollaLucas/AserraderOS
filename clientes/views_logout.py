from django.shortcuts import render
from django.contrib.auth import logout

# aca vamos a crear las views para los registros de los clientes
# logins, logout, etc.
# Vamos a tener un view para cada acción a realizar.

# LOGOUT

def pagina_logout(request):
    params={}
    logout(request)
    return render(request, "home.html", params)