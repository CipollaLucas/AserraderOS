"""
WSGI config for proyecto_aserradero project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# Recordar que esta variable le esta pegando al settings de LOCAL, si se quiere pasar a testing o produccion hay que modificar.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "proyecto_aserradero.settings.local")

application = get_wsgi_application()
