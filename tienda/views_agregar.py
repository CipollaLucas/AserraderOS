import json
from django.http import HttpResponse
from pedidos.models import Order

def agregar(request, *args, **kwargs):
    if request.method == "GET":  
        idpedido = request.GET.get("cada_pedido_id")
        valor = request.GET.get("valor")
        carro = request.session.get("carro")
        #En este caso vamos a tomar los valores
        #Acá a partir de la posicion 6 en adelante
        idpedido_rec = idpedido[6:]
        idpedido_rec = int(idpedido_rec)
        el_ped = Order.objects.get(id_pedido=idpedido_rec)
        print("idpedido_rec: ",idpedido_rec)
        print("El_ped: ",el_ped)
        #print(el_ped.stock)
        #print("stock")
        #stock_actual = int(el_ped.stock)

        #if int(valor) >= stock_actual:
        #    cantida = int(valor)
        #else:
        #    cantida = int(valor) + 1

        # ###########################################
        # ACTUALIZO VARIABLE DE SESSION
        # ###########################################

        #carro[idpedido] = cantida
        #request.session["carro"] = carro
        # ###########################################
        # FIN
        # ###########################################
        print(idpedido)
        print(valor)
        #print(cantida)
        print(carro)
        results = []
        data = {}
        data["idpedido"] = str(idpedido)
        #data["cantida"] = str(cantida)
        results.append(data)
        data_json = json.dumps(results)
        mimetype = "application/json"
        return HttpResponse(data_json, mimetype)