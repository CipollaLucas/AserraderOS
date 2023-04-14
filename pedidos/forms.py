from django.forms import ModelForm
from pedidos.models import Order
from django import forms

class SearchPedidoForm(forms.Form):
    querycom = forms.CharField(label="Ingresar el id del cliente", widget=forms.TextInput(attrs={'size': 32, 'class': 'form- control'}))



class CargarForm(ModelForm):
    class Meta:
        model = Order
        fields = ['id_pedido', 'id_cliente', 'descripcion', 'descri_foto', 'monto', 'estado_saldo']



    #Declaramos un constructor
    def __init__(self, *args, **kwargs):
        super(CargarForm, self).__init__(*args, **kwargs)