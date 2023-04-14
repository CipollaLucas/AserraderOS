Proyecto realizado en Django, con el interprete en la versión 3.10.8
Pasos a seguir para "levantar el proyecto de modo local"

IMPORTANTE: Tener instalado Django.

1: Clonar el repo del proyecto.

2: Crear entorno virtual en la carpeta raiz donde fue clonado el repo, luego ejecutarlo. (Asegurarse que esto funcione y que este dentro de el.)
    La librería viene instalada a partir a Python 3.3
    PARA CREAR EL ENTORNO:
                            - Debemos estar en el directorio que lo queremos instalar, 
                            y ejecutamos: python -m venv (nombre_del_entorno)
    
    PARA ACTIVAR EL ENTORNO:
                            - Ingresamos al directorio (nombre_del_entorno), y ejecutamos:
                            scripts\activate. 
                            Ahi denotara que la consola mostrará que ingresó al modo virtual.
    

3: Instalar los requerimientos y librerías necesarias, mediante la instrucción * pip install -r requirements.txt *. 
(en el caso de windows, en el caso de linux o powershell cambia el "pip" por "pip3")

4: Luego ejecutar en la consola con el entorno activado, 
dirigirnos a la carpeta donde se encuentra el manage.py 
y ejectuar: 
            - python manage.py makemigrations (Esto genera las migraciones correspondientes creando las tablas de la base de datos, etc.)
            - python manage.py migrate (Esto aplica las migraciones correspondientes)

            y por último levantamos en el puerto localhost:8000 o 127.0.0.01:8000 el proyecto con la siguiente instrucción:
            - python manage.py runserver

IMPORTANTE ****************

para poder ingresar al admin del backend, hay que crear un superUser:

en la consola ejecutamos:
                        - 1_) python manage.py createsuperuser
                        - 2_) Completar los campos que son obligatorios para el registro.
                        - 3_) Cuando la confirmación podemos correr el servidor nuevamente e ir http://127.0.0.1:8000/admin y tratar de ingresar. 


                            