# WEBEMPRESA
`pipenv run django-admin startproject webempresa`
`python manage.py startapp core`

**PREPARANDO EL BACKEND**

* En consola vscode
`activate django2`
    *(CursoDjango) deberia mostrar asi*

* Crear proyecto vscode
`django-admin startproject webempresa`

* Click derecho en manage.py 
'Ejecutar archivo Python en la terminal'
     *Elegir un entorno virtual*

* Crear las vistas en
**core/views.py** 

* Agregar en
**webempresa/core.py**
INSTALLED_APPS = [
    'core',
]


`python manage.py startapp services`

* Despues de crear cualquier modelo

`python manage.py makemigrations `
`python manage.py migrate`

`python manage.py createsuperuser`


* Crear configuracion basicas para el administrador en service/admin.py