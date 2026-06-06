# API Python FastAPI

## Descripción

Proyecto API REST desarrollado con Python y FastAPI.

## Tecnologías Utilizadas

* Python 3.x
* FastAPI
* Uvicorn
* SQLAlchemy
* MySQL

## Estructura del Proyecto

```text
project/
│
├── app/
│   ├── controllers/
│   ├── routes/
│   ├── schemas/
│   ├── models/
│   ├── config/
│   ├── utils/
│   └── main.py
│
├── requirements.txt
├── .gitignore
└── README.md
```

## Clonar el Repositorio

```bash
git clone git@github.com:chusRopero/senaFastApiViernes.git
```

Ingresar al proyecto:

```bash
cd senaFastApiViernes
```

## Crear Entorno Virtual

```bash
python -m venv venv
```

## Activar Entorno Virtual

### Linux / Ubuntu / Lubuntu / Debian

```bash
source venv/bin/activate
```

### Windows

```bash
venv\Scripts\activate
```

## Instalar Dependencias

```bash
pip install -r requirements.txt
```

## Ejecutar la Aplicación

```bash
uvicorn app.main:app --reload
```

## Acceder a la API

### Swagger UI

```text
http://127.0.0.1:8000/docs
```

### ReDoc

```text
http://127.0.0.1:8000/redoc
```

## Variables de Entorno

Crear un archivo `.env` en la raíz del proyecto.

Ejemplo:

```env
DB_HOST=localhost
DB_PORT=3306
DB_NAME=nombre_base_datos
DB_USER=usuario
DB_PASSWORD=contraseña
```

## Actualizar Dependencias

Si se agregan nuevas dependencias al proyecto:

```bash
pip freeze > requirements.txt
```

## Comandos Git

Verificar cambios:

```bash
git status
```

Agregar cambios:

```bash
git add .
```

Crear commit:

```bash
git commit -m "Descripción del cambio"
```

Subir cambios:

```bash
git push
```

## Autor

Jesus Ropero Barbosa

