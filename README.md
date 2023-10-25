# Proyecto de API REST con Flask y PostgreSQL

Este proyecto es una API REST desarrollada con Flask y PostgreSQL que permite gestionar usuarios y roles. Proporciona operaciones CRUD (Crear, Leer, Actualizar, Eliminar) para ambas entidades.

## Tecnologías Utilizadas

- Python
- Flask
- Blueprint
- Flask-SQLAlchemy
- PostgreSQL
- Flask-RESTful (opcional para rutas API REST)

## Prerequisitos

Para utilizar el API, se requiere instalar PostgresSQL y crear una BD de acuerdo con el siguiente modelo de datos:

https://github.com/udistrital/lineamientos_oas/blob/master/generacion_de_apis/img/002.png

## Instalación

Sigue estos pasos para configurar y ejecutar el proyecto en tu entorno local:

1. Clona el repositorio desde GitHub:

   ```bash
   git clone https://github.com/a52290451/prueba_api_flask_bp.git
   ```

2. Accede al directorio del proyecto:

```bash
   cd prueba_api_flask_bp
```

3. Crea un entorno virtual y actívalo:

```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate   
```

4. Instala las dependencias del proyecto:

```bash
   pip install -r requirements.txt  
```

5. Configura las variables de entorno en un archivo .env con la siguiente estructura:

> DB_USER_FBP= ****

> DB_PASSWORD_FBP= ****

> DB_HOST_FBP= ****

> DB_PORT_FBP= ****

> DB_NAME_FBP= ****`

Este archivo debe estar en la raiz del proyecto.

6. Ejecuta la aplicación:

```bash
   flask run  
```

La aplicación estará disponible en http://localhost:5000.

## Estructura de Archivos

**app.py**: Archivo principal de la aplicación.

**config.py**: Archivo de configuración para conexión a la BD.

**models.py**: Definición de modelos de base de datos.

**extensions.py**: Archivo que inicializa la BD con SQLAlchemy.

**rol/** */: Directorio que contiene el Blueprint para la entidad "Rol".

**rol/rol.py**: Blueprint con webservices de rol.

**usuario/** */: Directorio que contiene el Blueprint para la entidad "Usuario".

**usuario/usuario.py**: Blueprint con webservices de usuario.

**.gitignore**: elementos que serán ignorados a la hora de realizar actualizaciones en el repositorio.

**requirements.txt**: requerimientos para ejecutar el proyecto.
