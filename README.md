# Backend Homebanking Django

- [Configuración del proyecto](#instalación-del-proyecto)

## Instalación del proyecto

- Clonar el repositorio, acceder a la carpeta, y crear un entorno virtual.

```bash
  git clone https://github.com/AgusT613/itba_full_stack_back.git

  cd itba_full_stack_back

  python -m venv .venv
```

- Archivos del proyecto:

  - itba_full_stack_back/

    - app/
      - app/ (main)
      - login/
      - manage.py
    - .gitignore
    - README.md
    - requirements.txt

- Una vez hecho, acceder al instalador de paquetes de python (pip) desde el entorno virtual creado.

```bash
  source .venv/bin/activate
```

- Ahora se pueden instalar todos los paquetes necesarios para el proyecto desde el archivo `requirements.txt` usando el entorno virtual.

```bash
  pip install -r requirements.txt
```

- Acceder a la carpeta del proyecto `app` y crear los modelos de Django y aplicarlos a la base de datos (sqlite3)

```bash
  cd homebanking

  python manage.py makemigrations

  python manage.py migrate
```

- Por último, arrancar el servidor de desarrollo:

```bash
  python manage.py runserver
```
