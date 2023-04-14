import json
from django.shortcuts import render, HttpResponse
from django.urls import reverse_lazy
from django.core.serializers import serialize
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.generic.edit import FormView
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import CreateView
#Utilizamos las herramientas de Django para el logeo.
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from clientes.models import ClienteUsuario
from .forms import FormularioLogin, FormularioUsuario


# aca vamos a crear las views para los registros de los clientes
# logins, logout, etc.
# Vamos a tener un view para cada acción a realizar.

"""
Definimos la funcion is_ajax(), ya que no existe como tal.
def is_ajax(request):
  return request.headers.get('x-requested-with') == 'XMLHttpRequest'
"""

# LOGIN

def pagina_login(request):
    params={}
    #Como la información viene en un POST recuperamos los datos asi
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            print("NO ESTOY ENTRANDO.")
            return render(request, 'clientes/login.html', params)
            


    return render(request, "clientes/login.html", params)



def logoutUsuario(request):
    logout(request)
    return HttpResponseRedirect('home.html')


class ListadoUsuario(ListView):
    model = ClienteUsuario
    template_name = 'clientes/listar_usuarios.html'
    def get_queryset(self):
        return self.model.objects.filter(usuario_activo=True)
    
    """Para cualquier tipo de peticion del tipo GET, mandamos esta informacion mediante AJAX"""
"""    def get(self, request, *args, **kwargs):
       if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        if
            lista_usuarios = []
            for usuario in self.get_queryset():
                data_usuario = {}
                data_usuario['id'] = usuario.id
                data_usuario['nombre'] = usuario.nombre
                data_usuario['apellido'] = usuario.apellido
                data_usuario['email'] = usuario.email
                data_usuario['username'] = usuario.username
                data_usuario['cuit'] = usuario.cuit
                data_usuario['usuario_activo'] = usuario.usuario_activo
                lista_usuarios.append(data_usuario)
            data = json.dumps(lista_usuarios)
            return HttpResponse(data, 'application/json')
        else:
            return render(request, self.template_name)        
"""    


class RegistroUsuario(CreateView):
    model = ClienteUsuario
    form_class = FormularioUsuario
    template_name = 'clientes/registro.html'
    success_url = reverse_lazy('home')

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            nuevo_usuario = ClienteUsuario(
                email = form.cleaned_data.get('email'),
                username = form.cleaned_data.get('username'),
                nombre = form.cleaned_data.get('nombre'),
                apellido = form.cleaned_data.get('apellido'),
                cuit = form.cleaned_data.get('cuit'),
            )
            nuevo_usuario.set_password(form.cleaned_data.get('password1'))
            nuevo_usuario.save()
            return redirect('home')
        else:
            return render(request, self.template_name, {'form': form})
    

