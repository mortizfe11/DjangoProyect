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
4. Para ver el SQL que crea la tabla:
```
python3 manage.py sqlmigrate <nombre_de_tu_app> <numero_de_migración>
```

**SQLITE3**
1. Teniendo la extensión SQLite
2. Ejecutamos en Ver del Code: paleta de comandos
3. En comandos de > Sqlite > Quick Query hacemos
```
SELECT * FROM hello_world_app_member;
``` 


# Insetar datos en la BBDD
1. Abrimos la shell en interativo de Python y Django:
```
python3 manage.py shell
```
2. Importamos el modelo
```
from <nombre_de_la_app>.models import <clase_de_models>
```
3. Creamos un objeto.
Ejemplo:
```
from hello_world_app.models import Member
member = Member(firstname="Fulanito", lastname="Metepatas")
```
4. Guardamos con save:
```
member.save()
```