from django.shortcuts import render

# aca vamos a crear las views para los registros de los clientes
# logins, logout, etc.
# Vamos a tener un view para cada acción a realizar.

# PERFIL - Vamos a utilzar una clase.

def pagina_perfil(request):
    params={}
    return render(request, "clientes/mi_perfil.html", params)