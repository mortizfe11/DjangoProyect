### Create Deploy en Python anywhere

1. Clonamos el repositorio
```
git clone <nombre_repositorio>
```
2. Registramos el entorno virtual
```
python -m venv <nombre_entorno>
```
3. Activamos el entorno virtual
```
source <nombre_entorno>/bin/activate
```
4. Instalamos los requerimientos del .txt
```
pip install -r requirements.txt
```
5. Hacemos las migraciones en Django
```
python manage.py migrate
```
6. Generemos los estáticos de producción
```
python manage.py collectstatic
```
