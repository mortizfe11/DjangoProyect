# DjangoProyect

# Instalar Django

1. Virtual Environment
```
python3 -m venv myworld
source myworld/bin/activate
```
Virtual environment with pyenv
```
pyenv virtualenvs
pyenv virtualenv <num_version> <name_virtual_env>
pyenv <name_virtual_env> activate
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
```
codr
    manage.py
    codr/
        __init__.py
        asgi.py
        settings.py
        urls.py
        wsgi.py
```
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

# Creamos un superusuario
1. Ejecutamos en línea de comandos el siguiente comando:
```
python3 manage.py createsuperuser
```
2. Pruebas en loggearte en url/admin

# Cambiamos contraseña

```
python3 manage.py changepassword <nombre_de_usuariog>
```

# Archivos statics:
1. Añadimos el folder static
2. Añadimos el archivo .css en static

3. Instalamos whitenoise con:
```
pip install whitenoise
```
Y lo añadimos en settings.py:
```
MIDDLEWARES = [
    ...
    'whitenoise.middleware.WhiteNoiseMiddleware',
] 
```
4. Colocamos DEBUG en False (de settings.py):
```
DEBUG = False
```
6. Creamos la carpeta `productionfiles` dentro del proyecto
7. Y actualizamos settings.py con la ruta:
```
STATIC_ROOT = BASE_DIR / 'productionfiles'
STATIC_URL = '/static/'
```
8. Por último ejecutamos el comando collectstatic en consola para generar todos los archivos para la fase de producción:
```
python3 manage.py collectstatic
```
