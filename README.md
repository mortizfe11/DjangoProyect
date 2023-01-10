# DjangoProyect

# Instalar Django

1. Virtual Environment
```
python3 -m venv myworld
source myworld/bin/activate
```
2. Instalar Django
```
python3 -m pip install Django
```
3. Ver versión
```
django-admin --version 
```
4. Crear proyecto
```
django-admin startproject codr
```

5. Estructura del proyecto:

codr
    manage.py
    codr/
        __init__.py
        asgi.py
        settings.py
        urls.py
        wsgi.py

# Servidor de desarrollo
Abre por defecto en localhost puerto 8000.
```
python3 manage.py runserver
```

# Crear una app.

```
python3 manage.py startapp <nombre_de_tu_app>
```

# Crear un html:
1. Crear el archivo .html dentro de templates
2. Crear la función en views:
```
from django.template import loader
from django.http import HttpResponse

def hello_world(request):
    template = loader.get_template('hello_world.html')
    return HttpResponse(template.render())
```
3. Guardar la aplicación, colocándola en INSTALLED_APPS en settings.py
4. Ejecutar el siguiente comando para guardarlo en manage.py
```
python3 manage.py migrate
```

# Crear un modelo (que es una tabla en BBDD):
1. Crear la clase en models.py
2. Hacer la migración a la BBDD
```
python3 manage.py makemigrations <nombre_de_tu_app>
```
3. Ejecutar el siguiente comando para guardarlo en manage.py
```
python3 manage.py migrate
```
4. Para verlo
```
python3 manage.py sqlmigrate <nombre_de_tu_app> <numero_de_migración>
```
