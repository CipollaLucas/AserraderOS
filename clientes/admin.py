from django.contrib import admin
from clientes.models import ClienteUsuario



class ClienteUsuarioAdmin(admin.ModelAdmin):
    list_display = ('username', 'nombre', 'apellido', 'cuit')

admin.site.register(ClienteUsuario, ClienteUsuarioAdmin)