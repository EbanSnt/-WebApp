# -WebApp

![Python](https://img.shields.io/badge/Python-3.9-blue.svg)
![Django](https://img.shields.io/badge/Django-4.0-brightgreen.svg)
![Jinja2](https://img.shields.io/badge/Jinja2-3.0-brightgreen.svg)


![macOS](https://img.shields.io/badge/macOS-compatible-green)
![Linux](https://img.shields.io/badge/Linux-compatible-green)
![Windows](https://img.shields.io/badge/Windows-compatible-green)

Trabajo Grupal. Bootcamp Django - Alkemy. Caso de negocio N°2 - Biblioteca App🗃️:

## Autores

- [Adrian Martinez](https://github.com/adrian411997)
- [Eban Sánchez](https://github.com/EbanSnt)
- [Gaston](https://github.com/gaston010)
- [Robinson Sinner](https://github.com/RS4400)

Este es un proyecto de Biblioteca desarrollado con Django 4.0 y Jinja2.

## Estado del Proyecto

[![Build Status](https://img.shields.io/badge/Branch-develop-blue)](https://github.com/EbanSnt/-WebApp/tree/develop)

## Funcionalidades (Features)
 - Autores
    - [ ] Registro
    - [ ] Listado
    - [ ] Actualización
    - [ ] Eliminación
 - Libros
    - [ ] Registro
    - [ ] Listado
    - [ ] Actualización
    - [ ] Eliminación
 - Empleados
    - [x] Registro
    - [x] Listado
    - [x] Actualización
    - [ ] Eliminación
 - Socios
    - [ ] Registro
    - [x] Listado
    - [x] Actualización
    - [ ] Eliminación

## Requisitos previos

- Python 3.9 o superior
- Django 4.0
- Jinja2

## Configuración del entorno

1. Clona este repositorio en tu máquina local:

2. Ve al directorio del proyecto:

3. Crea un entorno virtual para el proyecto:

4. Activa el entorno virtual:

- En macOS y Linux:

  ```
  source nombre-env/bin/activate
  ```

- En Windows:

    ```
    nombre-env\Scripts\activate
    ```

5. Instala las dependencias del proyecto:

    ```
    pip install -r requirements.txt
    ```

6. Ejecuta las migraciones:

    ```
    python manage.py migrate
    ```

7. Crea un superusuario:

    ```
    python manage.py createsuperuser
    ```

8. Ejecuta el servidor de desarrollo:

    ```
    python manage.py runserver
    ```

9. Visita [http://localhost:8000/api](http://localhost:8000/api) en tu navegador.
