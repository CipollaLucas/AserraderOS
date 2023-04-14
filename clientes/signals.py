# Aqui vamos a poner el codigo de cosas que suceden con los clientes

"""
pre_save
post_save
Decorador que vamos a usar --> @receiver
"""

from django.db.models.signals import post_save
from django.dispatch import receiver
#from django.contrib.auth.models import User
from clientes.models import ClienteUsuario


"""# Un instante posterior a registar los datos de un usuario
@receiver(post_save, sender=ClienteUsuario)
#Vamos a hacer esto:
#Esta funcion tiene una instancia de este usuario, y a partir de ahi vamos a generar una registro de usuario. 
#Toma sender que es la clase de la cuál desprende ClienteUsuario
def create_usuariocliente(sender, instance, created, **kwargs):
    if created:
        ClienteUsuario.objects.create(username=instance)
        print("Se han creado los datos")
"""


"""@receiver (post_save, sender=ClienteUsuario)
def update_clienteusuario(sender, instance, **kwargs):
        instance.ClienteUsuario.save()
        print("Se han actualizado los datos")"""