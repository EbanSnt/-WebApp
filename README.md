# -WebApp

![Python](https://img.shields.io/badge/Python-3.9-blue.svg)
![Django](https://img.shields.io/badge/Django-4.0-brightgreen.svg)
![Jinja2](https://img.shields.io/badge/Jinja2-3.0-brightgreen.svg)

![macOS](https://img.shields.io/badge/macOS-compatible-green)
![Linux](https://img.shields.io/badge/Linux-compatible-green)
![Windows](https://img.shields.io/badge/Windows-compatible-green)

Trabajo Grupal. Bootcamp Django - Alkemy. Caso de negocio N°2 - Biblioteca App🗃️:

[Ir a la sección de Instalación](#instalacion)

[Documentacion](#documentacion)

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
  - [x] Registro
  - [x] Listado
  - [x] Actualización
  - [ ] Eliminación
- Libros
  - [x] Registro
  - [x] Listado
  - [x] Actualización
  - [ ] Eliminación
- Empleados
  - [x] Registro
  - [x] Listado
  - [x] Actualización
  - [ ] Eliminación
- Socios
  - [x] Registro
  - [x] Listado
  - [x] Actualización
  - [ ] Eliminación
- Prestamo de un Libro
  - [x] Registro
  - [x] Listado
  - [x] Actualización
  - [x] Eliminación

## Requisitos previos

- Python 3.9 o superior
- Django 4.0
- Jinja2

## Instalacion

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

## Documentacion

## Listados de Endpoints

[Autores](#) |   [Libros](#) |  [Empleados](# )   |   [Socios](#) |  [Prestamos](#)

## Endpoints

<details>
<summary>Autores</summary>

## Endpoints de Autores

| Método | Endpoint | Descripción |
| ------ | -------- | ----------- |
| GET    | /api/autores/ | Listado de autores |
| POST   | /api/autores/nuevo | Crear un autor |
| GET    | /api/autores/{id}/ | Obtener un autor |
| PUT    | /api/autores/{id}/modificarr | Actualizar un autor |
| DELETE | /api/autores/{id}/eliminar | Eliminar un autor |

</details>

<details>
<summary>Libros</summary>

## Endpoints de Libros

| Método | Endpoint | Descripción |
| ------ | -------- | ----------- |
| GET    | /api/libros/ | Listado de libros |
| POST   | /api/libros/nuevo | Crear un libro |
| GET    | /api/libros/{id}/ | Obtener un libro |
| PUT    | /api/libros/{id}/modificar | Actualizar un libro |
| DELETE | /api/libros/{id}/eliminar | Eliminar un libro |

</details>

<details>
<summary>Empleados</summary>

## Endpoints de Empleados

| Método | Endpoint | Descripción |
| ------ | -------- | ----------- |
| GET    | /api/empleados/ | Listado de empleados |
| POST   | /api/empleados/nuevo | Crear un empleado |
| GET    | /api/empleados/{id}/ | Obtener un empleado |
| PUT    | /api/empleados/{id}/modificar | Actualizar un empleado |
| DELETE | /api/empleados/{id}/eliminar | Eliminar un empleado |

</details>

<details>
<summary>Socios</summary>

## Endpoints de Socios

| Método | Endpoint | Descripción |
| ------ | -------- | ----------- |
| GET    | /api/socios/ | Listado de socios |
| POST   | /api/socios/nuevo | Crear un socio |
| GET    | /api/socios/{id}/ | Obtener un socio |
| PUT    | /api/socios/{id}/modificar | Actualizar un socio |
| DELETE | /api/socios/{id}/eliminar | Eliminar un socio |

</details>

<details>
<summary>Prestamos</summary>

## Endpoints de Prestamos

| Método | Endpoint | Descripción |
| ------ | -------- | ----------- |
| GET    | /api/prestamos/ | Listado de prestamos |
| POST   | /api/prestamos/nuevo | Crear un prestamo |
| GET    | /api/prestamos/{id}/ | Obtener un prestamo |
| PUT    | /api/prestamos/{id}/modificar | Actualizar un prestamo |
| DELETE | /api/prestamos/{id}/eliminar | Eliminar un prestamo |

</details>

# Vistas Generales

<details>
<summary>Autor Vistas</summary>

## Autor Lista

### GET /api/autores/

<p> Retorna una lista de los autores registrados en la base de datos. </p>

```python
    try:
        autores = Autor.objects.all()
        context = {"autores": autores }
        return render(request, "autor_lista.html", context)
    except Exception:
         return render(request, "autor_lista.html")
```

<details>

<summary> Registro</summary>

## Autor Nuevo

### POST /api/autores/nuevo

<p> Mediante un formulario ingresa/registra un nuevo autor en la base de datos </p>

```python
    if request.method == "POST":
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("autor_lista")
    else:
        form = AutorForm()
    return render(request, "autor_nuevo.html", {"form": form})
```

</details>
<details>

## Autor Modificar

<summary> Actualización</summary>

### PUT /api/autores/{id}/modificar

<p>Obteniendo los datos ya cargados desde la base de datos nos proporciona un nuevo formulario en el cual podemos modificar los datos neccesarios para actualizar nuestro Autor</p>

```python
    autor = Autor.objects.get(id=id)
    if request.method =="POST": 
        autor.nombre = request.POST["nombre"]
        autor.apellido = request.POST["apellido"]
        autor.nacionalidad= request.POST["nacionalidad"]
        if request.POST.get("activo") == None:
            autor.activo = False
        else:
            autor.activo = True
        autor.save()
        return redirect("autor_lista")
    else:
        return render(request,"autores_actualizar.html",{"autor":autor})
```

</details>
</details>

<details>

<summary> Empleado Vistas</summary>

<details>

<summary> Lista</summary>

## Empleado Lista

### GET /api/empleados/

<p>Retorna una lista de los empleados registrados en la base de datos. </p>

```python
    try:
        empleados = Empleado.objects.all()
        context = {"empleados": empleados }
        return render(request, "empleado_lista.html", context)
    except Exception:
         return render(request, "empleado_lista.html")
```

</details>

<details>
<summary> Registro</summary>

### POST /api/empleados/nuevo

<p> Registro de un nuevo empleado en la base de datos</p>

```python
    if request.method == "POST":
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("empleado_lista")
    else:
        form = EmpleadoForm()
    return render(request, "empleado_nuevo.html", {"form": form})
```

</details>

<details>
<summary> Actualización</summary>

### PUT /api/empleados/{id}/modificar

<p>Obteniendo los datos ya cargados desde la base de datos nos proporciona un nuevo formulario en el cual podemos modificar los datos neccesarios para actualizar nuestro Empleado</p>

```python
    empleado = Empleado.objects.get(id=id)
    if request.method =="POST": 
        empleado.nombre = request.POST["nombre"]
        empleado.apellido = request.POST["apellido"]
        empleado.dni= request.POST["dni"]
        empleado.telefono = request.POST["telefono"]
        empleado.email = request.POST["email"]
        empleado.direccion = request.POST["direccion"]
        empleado.save()
        return redirect("empleado_lista")
    else:
        return render(request,"empleado_actualizar.html",{"empleado":empleado})
```

<details>
<summary> Eliminación</summary>

### DELETE /api/empleados/{id}/eliminar

</details>
</details>
</details>

<details>
<summary> Socio Vistas</summary>

<details>
<summary> Lista</summary>

## Socio Lista

### GET /api/socios/

<p>Lista de los socios obenida desde la base de datos</p>

```python
    try:
        socios = Socio.objects.all()
        context = {"socios": socios }
        return render(request, "socio_lista.html", context)
    except Exception:
         return render(request, "socio_lista.html")
```

</details>

<details>
<summary> Registro</summary>

## Socio Nuevo

### POST /api/socios/nuevo

<p>Mediante un formulario ingresa/registra un nuevo autor en la base de datos</p>

```python
    if request.method == "POST":
        form = SocioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("socio_lista")
    else:
        form = SocioForm()
    return render(request, "socio_nuevo.html", {"form": form})
```

</details>

<details>
<summary> Actualización</summary>

## Socio Modificar

### PUT /api/socios/{id}/modificar

<p>Obteniendo los datos ya cargados desde la base de datos nos proporciona un nuevo formulario en el cual podemos modificar los datos neccesarios para actualizar nuestro Empleado</p>

```python
    socio = Socio.objects.get(id=id)
    if request.method =="POST": 
        socio.nombre = request.POST["nombre"]
        socio.apellido = request.POST["apellido"]
        socio.dni= request.POST["dni"]
        socio.telefono = request.POST["telefono"]
        socio.email = request.POST["email"]
        socio.direccion = request.POST["direccion"]
        socio.save()
        return redirect("socio_lista")
    else:
        return render(request,"socio_actualizar.html",{"socio":socio})
```

</details>

<details>
<summary> Eliminación</summary>

### DELETE /api/socios/{id}/eliminar

<p></p>

</details>

<details>
<summary> JSON</summary>

</details>
</details>

<details>

<summary> Libro Vistas</summary>

<details>

<summary> Lista</summary>

## Libro Lista

### GET /api/libros/

<p>Lista de los libros obenida desde la base de datos</p>

```python
    try:
        libros = Libro.objects.all()
        context = {"libros": libros }
        return render(request, "libro_lista.html", context)
    except Exception:
         return render(request, "libro_lista.html")
```

</details>

<details>
<summary> Registro</summary>

## Libro Nuevo

### POST /api/libros/nuevo

<p>Registra un nuevo socio en la base de datos mediante un formulario desde la App</p>

```python
    if request.method == "POST":
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("libro_lista")
    else:
        form = LibroForm()
    return render(request, "libro_nuevo.html", {"form": form})
```

</details>

<details>

<summary> Actualización</summary>

## Libro Modificar

### PUT /api/libros/{id}/modificar

<p></p>

```python
    libro = Libro.objects.get(id=id)
    if request.method =="POST": 
        libro.titulo = request.POST["titulo"]
        libro.autor = request.POST["autor"]
        libro.editorial = request.POST["editorial"]
        libro.genero = request.POST["genero"]
        libro.save()
        return redirect("libro_lista")
    else:
        return render(request,"libro_actualizar.html",{"libro":libro})
```

</details>

<details>
<summary> Eliminación</summary>

</details>
</details>


<details>

<summary> Prestamo Vistas</summary>

<details>

<summary> Lista</summary>

## Prestamo Lista

### GET /api/prestamos/

<p>Proporciona una lista de un prestamo de libros, el mismo nos trae datos desde las tabla de Socio, Emplead y libro asi como una fecha de prestamo y entrega del mismo</p>

```python
    try:
        prestamos = Prestamo.objects.all()
        context = {"prestamos": prestamos }
        return render(request, "prestamo_lista.html", context)
    except Exception:
         return render(request, "prestamo_lista.html")
```

</details>


<details>

<summary> Registro</summary>

## Prestamo Nuevo

### POST /api/prestamos/nuevo

<p>Mediante un formulario ingresa/registra un nuevo autor en la base de datos.
Los datos tomados son obtenidos de las tablas de Libro y Socio con una fecha de prestamo y de entrega siendo la misma 2 dias despues del prestamo</p>

```python
    if request.method == "POST":
        form = PrestamoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("prestamo_lista")
    else:
        form = PrestamoForm()
    return render(request, "prestamo_nuevo.html", {"form": form})
```

</details>

<details>

<summary> Actualización</summary>

## Prestamo Modificar

### PUT /api/prestamos/{id}/modificar

<p>Obteniendo los datos ya cargados desde la base de datos nos proporciona un nuevo formulario en el cual podemos modificar los datos neccesarios para actualizar nuestro Empleado</p>

```python
    prestamo = Prestamo.objects.get(id=id)
    if request.method =="POST": 
        prestamo.socio = request.POST["socio"]
        prestamo.empleado = request.POST["empleado"]
        prestamo.libro = request.POST["libro"]
        prestamo.fecha_prestamo = request.POST["fecha_prestamo"]
        prestamo.fecha_entrega = request.POST["fecha_entrega"]
        prestamo.save()
        return redirect("prestamo_lista")
    else:
        return render(request,"prestamo_actualizar.html",{"prestamo":prestamo})
```

</details>

<details>

<summary> Eliminación</summary>


### DELETE /api/prestamos/{id}/eliminar

<p>Eliminacion de un prestamo, la misma tira error si el proceso no es completado correctamente</p>

```python
try:
    prestamo = get_object_or_404(Prestamo_libro, id=id) 
    if request.method == "POST":
        prestamo.delete()
        messages.success(request, "El préstamo ha sido eliminado exitosamente.")
        return redirect("prestamos_lista") #
    return render(request, "borrar_prestamo_libro.html", {"prestamo": prestamo})
except Exception as e:
    return redirect("error")
```

</details>
