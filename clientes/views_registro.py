from django.shortcuts import render, redirect
from clientes.forms import CreateUserForm

# aca vamos a crear las views para los registros de los clientes
# logins, logout, etc.
# Vamos a tener un view para cada acción a realizar.

# Registro de clientes

def pagina_registro(request):
    params={}
    #aca guardamos el formulario. Y lo mandamos a la vista.
    form=CreateUserForm()
    params['form'] = form

    #Si ese formulario viene vía POST.
    #Vamos a tomar los datos del formulario
    if request.method == 'POST':
        form=CreateUserForm(request.POST)
        #Chequeamos que sea correcto el formulario
        if form.is_valid():
            form.save()
            print("User created")
            return redirect('templates/home.html')
        else:
            print("User not found")
            return render('templates/home.html')


    return render(request, "clientes/registro.html", params)