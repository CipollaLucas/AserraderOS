from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.

#Creamos la clase para poder crear a los Users
class UsuarioManager(BaseUserManager):
    def _create_user(self, email, username, cuit, nombre, apellido, password = None):
        if not email:
            raise ValueError('El usuario debe tener email.')
        
        user = self.model(
            username=username,  
            email=self.normalize_email(email), 
            cuit=cuit, 
            nombre=nombre, 
            apellido=apellido,
            )

        user.set_password(password)
        user.save()
        return user


    #Creamos superUser
    def create_superuser(self, username, email, cuit, nombre, apellido, password):
        user = self._create_user(
            email,
            username=username,
            cuit=cuit,
            nombre=nombre,  
            apellido=apellido,
            #Le pasamos la password porque sino quedan en None.
            password=password,
        ) 
        user.usuario_administrador = True
        user.save()
        return user

class ClienteUsuario(AbstractBaseUser):
    username             = models.CharField('Nombre de usuario', unique=True, max_length=100)
    email                = models.EmailField('Correo electrónico', unique=True, max_length=254, blank=True)
    cuit                 = models.CharField('CUIT/CUIL', unique=True, max_length=30)
    nombre               = models.CharField('Nombre', max_length=50, default='', blank=True)
    apellido             = models.CharField('Apellido',max_length=50, default='', blank=True)
    descripcion          = models.CharField(max_length=200, default='NO TIENE DECRIPCION O ES NUEVO')
    fecha_nacimiento     = models.DateField(blank=True, null=True)
    provincia            = models.CharField(max_length=40, blank=True)
    ciudad               = models.CharField(max_length=40, blank=True)
    domicilio            = models.CharField(max_length=80, blank=True)
    codigo_postal        = models.CharField(max_length=50, blank=True)
    telefono             = models.CharField('Telefono', max_length=30, blank=True)
    celular              = models.CharField('Celular', max_length=30, blank=True)
    usuario_activo       = models.BooleanField(default=True)    
    usuario_administrador = models.BooleanField(default=False)
    
    objects = UsuarioManager()


    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'cuit','nombre', 'apellido' ]
    
    def __str__(self):
        return f'{self.nombre} {self.apellido} - {self.cuit}'
    
    #Método para poder acceder al admin de django.
    def has_perm(self, perm, obj = None):
        return True
    
    def has_module_perms(self, app_label):
        return True
    
    @property
    def is_staff(self):
        return self.usuario_administrador


