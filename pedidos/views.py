# VIEW.PY Contiene la lógica o funcionalidad de la aplicación.

from django.shortcuts import render
from django.http import HttpResponse



#Acá encontramos nuestras templates con sus referencias 


def home(request):
    return render(request, "home.html")


def productos(request):
    return render(request, "productos.html")


def servicios(request):
    return render(request, "servicios.html")


def pedidos(request):
    return render(request, "pedidos.html")


def about(request):
    return render(request, "about.html")

