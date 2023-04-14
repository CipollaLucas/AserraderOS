#en este formulario vamos a crear a los usuarios
from django import forms
from django.contrib.auth.forms import AuthenticationForm
#from django.contrib.auth.models import User
from clientes.models import ClienteUsuario


class FormularioLogin(AuthenticationForm):
    def __init__(self,  *args, **kwargs) :
        super(FormularioLogin).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Nombre de usuario'
        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['placeholder'] = 'Contraseña'

"""
Formulario de registro de un usuario en la base de datos
"""    
class FormularioUsuario(forms.ModelForm):
    """"
        Variables:
        - password1 = Contraseña
        - password2 = Verificación de contraseña
    """
    password1 = forms.CharField(label='Contraseña',widget=forms.PasswordInput(
        attrs = {
            'class': 'form-control',
            'placeholder': 'Ingrese la contraseña...',
            'id' : 'password1',
            'required' : 'required',
        }
    ))
    password2 = forms.CharField(label='Confirme contraseña',widget=forms.PasswordInput(
        attrs = {
            'class': 'form-control',
            'placeholder': 'Reingrese la contraseña...',
            'id' : 'password2',
            'required' : 'required',
        }
    ))

    class Meta:
        model = ClienteUsuario
        fields = ( 'username', 'email', 'nombre', 'apellido', 'cuit')
        widget = {
            'username': forms.TextInput(
            attrs= {
                'class': 'form-control',
                'placeholder': 'Escoja su nombre de usuario(se recomienda "nombre.apellido")',
                }
            ),
            'email': forms.EmailInput(
            attrs= {
                'class': 'form-control',
                'placeholder': 'Correo electrónico',
                }
            ),
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su nombre',
                }
            ),
            'apellido': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su apellido',
                }
            ),
            'cuit': forms.IntegerField(
                help_text="Ingrese su cuit/cuil",
            ),
        }

def clean_field(self):
    """
    Validación de la contraseña

    Método que verifica que las contraseñas ingresadas sean iguales, antes de ser encriptadas y guardadas en la base de datos.
    Retorna la contraseña válida.

    Excepciones
    - ValidationError -- cuando las contraseñas sean diferentes.
    """
    password1 = self.cleaned_data.get ('password1')
    password2 = self.cleaned_data.get ('password2')
    
    if password1 and password2 and password1 != password2:
        raise forms.ValidationError('Contraseñas no coinciden')
    return password2
    




"""
    El parametro commit en True, invoca al metodo save y guarda,
    Cambiando a false, guarda la instancia con la informacion. En este caso en user
def save(self, commit = True):
    user = user.save(commit=False)
    user.set_password(self.cleaned_data['password1'])
    if commit:
        user.save()
    return user
"""