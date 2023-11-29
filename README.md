# Backend Homebanking Django

- [Configuración del proyecto](#instalación-del-proyecto)
- [Credenciales de base de datos](#credenciales)

## Instalación del proyecto

- Clonar el repositorio, acceder a la carpeta, y crear un entorno virtual.
- En este ejemplo se usó git bash.
- Los comandos pueden variar dependiendo de la terminal usada. Para información más detallada visitar la [documentacion de .venv](https://docs.python.org/3/library/venv.html).

```bash
  git clone https://github.com/AgusT613/itba_full_stack_back.git

  cd itba_full_stack_back

  python -m venv .venv
```

- Archivos del proyecto:

  - itba_full_stack_back/

    - app/
      - app/ (main)
      - cuentas/
      - facturas/
      - login/
      - pagos/
      - prestamos/
      - tarjetas/
      - db.sqlite3
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

- Por último, arrancar el servidor de desarrollo:

```bash
  python manage.py runserver
```

## Credenciales

Creadas para testear la aplicación

```json
{
  username = agust613
  password = agustin123
},
{
  username = pablo
  password = pablo123
}
```
