from django.db import models
from clientes.models import ClienteUsuario
from django.utils.html import format_html


#Creamos los modelos correspondientes

class Order(models.Model):
    # Acá agregamos una tupla para identificar el estado del pedido.
    INGRESADO = 'Ingresado'
    ENPROCESO = 'En proceso'
    LISTO = 'Listo'
    FINALIZADO = 'Entregado'
    DEVOLUCION = (
        (INGRESADO, "Ingresado"),
        (ENPROCESO, "En proceso"),
        (LISTO, "Listo"),
        (FINALIZADO, "Entregado"),
    )

    id_pedido = models.AutoField(primary_key=True, blank=True)
    id_cliente=models.OneToOneField(ClienteUsuario, blank=False, null=True, on_delete=models.CASCADE)
    fecha_ingreso=models.DateTimeField(auto_now_add=True)
    update=models.DateTimeField(auto_now=True)
    descripcion=models.TextField(blank=True)
    descri_foto=models.ImageField(blank=True)
    monto=models.IntegerField(null=True, blank=True)
    estado_pedido = models.CharField(
        max_length=15,blank=True, choices=DEVOLUCION, default=INGRESADO
    )
    

    #Con este metodo retornamos en modo string lo que queremos ver en la pantalla de lista de pedidos del objeto Order.
    #También como recibe la shell si queremos consultar.
    def __str__(self):
        return "ID pedido: " + str(self.id_pedido) + " Cliente: " + str(self.id_cliente)
    
    
    # Vamos a trabajar sobre el estado. Agregamos funcionalidad por medio de un metodo.
    # Con el adobe kuller podemos crear colores.
    # EN EL .ADMIN cuando queremos mostrar en el list_display, HAY QUE LLAMARLO POR ESTE METODO
    def estado_de_pedido(self):
        if self.estado_pedido == 'Ingresado':
            return format_html('<span style="background-color:#09A5E6; color: #fff; padding:5px;">{}</span>' , self.estado_pedido, )
        elif self.estado_pedido == 'En proceso':
            return format_html('<span style="background-color:#FC495B; color: #fff; padding:5px;> {}</span>', self.estado_pedido, )
        elif self.estado_pedido == 'Listo':
            return format_html('<span style="background-color:#0AE456; color: #fff; padding:5px;">{}</span>', self.estado_pedido, )
        elif self.estado_pedido == 'Entregado' :
            return format_html('<span style="background-color:#FE703D; color: #fff; padding:5px;"> {}</span>', self.estado_pedido, )
    
    # Acá agregamos una tupla para identificar el estado economico del pedido.
    Sinseña = "Sin seña"
    Señado = "Señado"
    Pagado = "Pagado"
    ESTADO_SALDO = (
        (Sinseña, "Sin seña"),
        (Señado, "Señado"),
        (Pagado, "Pagado"),
    )

    estado_saldo = models.CharField(
        max_length=10, choices=ESTADO_SALDO, default=Sinseña
    )

    def estado_de_saldo(self):
        if self.estado_saldo == 'Sin seña':
            return format_html('<span style="background-color:#E64B37; color: #fff; padding:5px;">{}</span>' , self.estado_saldo, )
        elif self.estado_saldo == 'Señado':
            return format_html('<span style="background-color:#FFE830; color: #fff; padding:5px;> {}</span>', self.estado_saldo, )
        elif self.estado_saldo == 'Pagado':
            return format_html('<span style="background-color:#0a0; color: #fff; padding:5px;">{}</span>', self.estado_saldo, )

    class Meta:
        verbose_name = "pedido"
        verbose_name_plural = "pedidos"
        ordering = ["fecha_ingreso"]

    







