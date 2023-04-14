from django.shortcuts import render
from tienda.forms import CargarForm
from pedidos.forms import SearchPedidoForm
from pedidos.models import Order
from django.shortcuts import redirect
from django.http import Http404, HttpResponse
import json
from django.template import loader

from django.views import View


def cargar_imagen(request):
#En este metodo vamos a cargar los pedidos
#Vamos a pasar informacion
#La informacion viaja a travez de la URL,lo hace mediante un array de información llamada GET, cuando no viaja atraves de la URL lo hace con un array llamado POST
#Los formularios aún cuando sea interno, haciendo una template, se renderiza con datos que van a traves de la URL. 
#Mientras apreta enviar, tiene que ser enviado por medio de POST (es más reervado)

    params={}
    #Traemos la info del formulario, y preguntamos si la consulta es igual a POST
    if request.method == 'POST':
        form = CargarForm(request.POST, request.FILES)
        params['form'] = form
        #Validamos la informacion respecto al modelo.
        if form.is_valid():
            #pedido = form.cleaned_data['id_pedido']
            cliente = form.cleaned_data['id_cliente']
            descripcion = form.cleaned_data['descripcion']
            descri_foto = form.cleaned_data['descri_foto']
            monto = form.cleaned_data['monto']
            seña = form.cleaned_data['estado_saldo']

            nuevo_pedido = Order(id_cliente=cliente, descripcion=descripcion, descri_foto=descri_foto, monto=monto, estado_saldo=seña)
            nuevo_pedido.save()
            return redirect('home')

    else:
        form = CargarForm()
        params['form'] = form
        return render(request, 'tienda/formulario.html', params)

class VerImagenes(View):
    template = "tienda/verimagenes.html"

    def get(self, request):
        #Por si queremos enviar informacion a esta vista.
        params={}
        try:
            pedidos = Order.objects.all()
        except Order.DoesNotExist:
            raise Http404
        params["pedidos"] = pedidos

        return render(request, self.template, params)

def ver_imagen(request, pedido_id): 
    #Aca enviamos informacion al template
    params = {}
    try:
        #Acá vamos a traer el pedido por ID.
        pedido = Order.objects.get(pk=pedido_id)
    except Order.DoesNotExist:
        raise Http404
    params["pedido"] = pedido

    return render(request, "tienda/verimagen.html", params)



#Creamos una clase administardora para el CRUD en localStorage
class EjemploLocalStorage(View):
    template = "tienda/localstorage.html"

    #Vamos a la página con get
    def get(self, request):
        params= {}   
        try:
            pedidos = Order.objects.all()
        except Order.DoesNotExist:
            raise Http404
        
        #Le mandamos los pedudos a la vista
        params["pedidos"] = pedidos
        #########################################################
        # Para inicializar las variables de sesion
        #########################################################

        #Acá intenta atrapar la variable de sesion
        try:
            request.session["carro"]
        except:
            request.session["carro"] = {}

        return render(request, self.template, params)


class views_agregar(View):
    pass

def para_ajax(request):

    params = {}
    search = SearchPedidoForm()
    params['search'] = search

    return render(request, 'tienda/ver_ajax.html', params)

#Generamos la clase para buscar el pedido
class buscarpedido(View):
    #La info va a venir mediante get
    def get(self, request):

        #Si la info viene mediante ajax
        if request.is_ajax:
            #Tomamos la palabra que este trayendo el request
            palabra = request.GET.get('term', '')
            #lo busca aqui dentro.
            pedidos = Order.objects.filter(id_cliente__icontains = palabra)
            #pedidos = Order.objects.filter(id_cliente = palabra)
            result = []
            #Acá me va a traer todos los pedidos que tengan ese termino
            #Crea un listado y me lo envia en formato JSON"""
            for an in pedidos:
                data={}
                data['label']=an.id_pedido
                result.append(data)
            data_json = json.dumps(result)
        else:
            data_json = "Error"
            print("Sale por aca")
        #Usamos el mimetype para que todo el tiempo este mandando al servidor y recibiendo.
        mimetype='application/json'
        return HttpResponse(data_json, mimetype)

#Generamos la clase para buscar el pedido
class buscarpedido2(View):
    #La info va a venir mediante get
    def get(self, request):

        #Si la info viene mediante ajax
        if request.is_ajax:
            #Yas sabemos cual es la clave
            q = request.GET['valor']
            #lo busca aqui dentro.
            pedido = Order.objects.filter(id_pedido__icontains=q)
            results = []
            #Acá me va a traer todos los pedidos que tengan ese termino
            #Crea un listado y me lo envia en formato JSON"""
            for rec in pedido:
                print(rec.id_pedido)
                print(rec.id_cliente)
                print(rec.descripcion)
                data={}
                data['id_pedido']=rec.id_pedido
                data['estado']=rec.id_cliente
                data['descripcion']=rec.descripcion
                results.append(data)
            data_json = json.dumps(results)
        else:
            data_json = "Fallo"
            print("Sale por aca")
        #Usamos el mimetype para que todo el tiempo este mandando al servidor y recibiendo.
        mimetype='application/json'
        return HttpResponse(data_json, mimetype)