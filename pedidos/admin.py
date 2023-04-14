from django.contrib import admin
from .models import Order
from django.core.exceptions import ObjectDoesNotExist    
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render

# Aca podemos modificar la vista de cuando queremos editar un registro.

class OrderAdmin(admin.ModelAdmin):

    # Con list display, ordenamos la vista como deseamos en la pestaña pedidos.
    # este comando pisa al método __str__ del models.py
    # OJO de confundir el nombre de los metodos de models.py con respecto a los fields para mostrar.

    list_display = ['id_pedido','id_cliente','estado_de_pedido','estado_de_saldo', 'fecha_ingreso']

    list_filter = ['fecha_ingreso']
    actions=["entregar", "enproceso", "listo", "exportar_a_json", "ver_pedidos"]
    def entregar(self, request, queryset):
        registro = queryset.update(estado_pedido="Entregado")
        if registro == 1:
            mensaje =  " 1 registro actualizado"
        else:
            mensaje = "%s registros actualizados" % registro
        self.message_user(request, "%s exitosamente" % mensaje)
    entregar.short_description = 'Pasar a entregado'

    def enproceso(self, request, queryset):
        queryset.update(estado_pedido="En proceso")
    enproceso.short_description = 'Pasar a en proceso'
    def listo(self, request, queryset):
        queryset.update(estado_pedido="Listo")
    listo.short_description = 'Pasar a listo (a la espera de ser retirado)'

    def ver_pedidos(self, request, queryset):
        params = {}
        pedidos=Order.objects.all
        params['pedidos'] = pedidos
        return render(request, "admin/pedidos/pedidos.html", params)
    ver_pedidos.short_description = "Ver pedidos en una pagina"

    def exportar_a_json(self, request, queryset):
        response = HttpResponse(content_type="application/json")
        serializers.serialize("json", queryset, stream=response)
        return response


"""class ClienteAdmin(admin.ModelAdmin):
    list_display = [
        'usuario',
        'nombre',
        'apellido',
        'cuit',
    ]
"""





admin.site.register(Order, OrderAdmin)
#admin.site.register(Cliente, ClienteAdmin)