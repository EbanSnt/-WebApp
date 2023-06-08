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

## Listados de Endpoints

[Autores](#endpoints-de-autores) |   [Libros](#endpoints-de-libros) |  [Empleados](#endpoints-de-empleados)   |   [Socios](#endpoints-de-socios) |  [Prestamos](#endpoins-de-prestamos)

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

## Endpoints

# *Autores*

## Endpoints de Autores

| Método | Endpoint | Descripción |
| ------ | -------- | ----------- |
| GET    | [/home/autores/](#autor-vistas)| Listado de autores |
| POST   | [/home/autores/nuevo](#autor-registro) | Crear un autor |
| GET    | [/api/autores/{id}/](#) | Obtener un autor |
| PUT    | [/home/autores/{id}/modificar](#autor-modificar) | Actualizar un autor |
| DELETE | [/home/autores/{id}/eliminar](#autor-eliminar) | Eliminar un autor |
# *Empleados*
##### Endpoints de Empleados

| Método | Endpoint | Descripción |
| ------ | -------- | ----------- |
| GET    | [/home/empleados/](#empleado-vistas) | Listado de empleados |
| POST   | [/home/empleados/nuevo](#empleado-registro) | Crear un empleado |
| GET    | /api/empleados/{id}/ | Obtener un empleado |
| PUT    | [/home/empleados/{id}/modificar](#empleado-modificar) | Actualizar un empleado |
| DELETE | [/home/empleados/{id}/eliminar](#empleado-eliminar) | Eliminar un empleado |

# *Socios*

#### Endpoints de Socios

| Método | Endpoint | Descripción |
| ------ | -------- | ----------- |
| GET    | [/home/socios/](#socio-lista) | Listado de socios |
| POST   | [/home/socios/nuevo](#socio-registro) | Crear un socio |
| GET    | /api/socios/{id}/ | Obtener un socio |
| PUT    | [/home/socios/{id}/modificar](#socio-modificar) | Actualizar un socio |
| DELETE | /home/socios/{id}/eliminar | Eliminar un socio |
# *Libros*

## Endpoints de Libros

| Método | Endpoint | Descripción |
| ------ | -------- | ----------- |
| GET    | [/home/libros/](#libro-vistas) | Listado de libros |
| POST   | [/home/libros/nuevo](#libro-registro) | Crear un libro |
| GET    | /api/libros/{id}/ | Obtener un libro |
| PUT    | [/home/libros/{id}/modificar](#libro-modificar) | Actualizar un libro |
| DELETE | [/home/libros/{id}/eliminar](#libro-eliminar) | Eliminar un libro |

# Prestamos

#### Endpoints de Prestamos

| Método | Endpoint | Descripción |
| ------ | -------- | ----------- |
| GET    | [/home/prestamos/](#prestamo-vistas) | Listado de prestamos |
| POST   | [/home/prestamos/nuevo](#prestamo-registro) | Crear un prestamo |
| GET    | [/api/prestamos/{id}/] | Obtener un prestamo |
| PUT    | [/home/prestamos/{id}/modificar](#prestamo-modificar) | Actualizar un prestamo |
| DELETE | [/home/prestamos/{id}/eliminar](#prestamo-eliiminar) | Eliminar un prestamo |

# *Vistas Generales*

# __Autor Vistas__

- Autor Lista

- GET /home/autores/

<p> Retorna una lista de los autores registrados en la base de datos. </p>

```python
    try:
        autores = Autor.objects.all()
        context = {"autores": autores }
        return render(request, "autor_lista.html", context)
    except Exception:
         return render(request, "autor_lista.html")
```

# Autor Registro

- Autor Nuevo

- POST /home/autores/nuevo

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

## Autor Modificar

- Actualización

- PUT /home/autores/{id}/modificar

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

# __Empleado Vistas__

- Lista

- Empleado Lista

- GET /home/empleados/

<p>Retorna una lista de los empleados registrados en la base de datos. </p>

```python
    try:
        empleados = Empleado.objects.all()
        context = {"empleados": empleados }
        return render(request, "empleado_lista.html", context)
    except Exception:
         return render(request, "empleado_lista.html")
```

# Empleado Registro

- POST /home/empleados/nuevo

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

# Empleado Modificar

- PUT /home/empleados/{id}/modificar

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

# Empleado Eliminar

- DELETE /home/empleados/{id}/eliminar

# __Socio Vistas__
## URLS

![179](https://github.com/EbanSnt/-WebApp/assets/113145320/f662a9ca-05f1-4199-ad68-64d63be3137f)

![180](https://github.com/EbanSnt/-WebApp/assets/113145320/ce4fc9e1-6954-4e4c-b47e-e77713930e3d)

![181](https://github.com/EbanSnt/-WebApp/assets/113145320/4005a341-20f1-4e28-815e-7305f80a90f3)


```python
    #LIBROS
    path("libros/nuevo/", registrar_libro,name="registrar_libro"),
    path("libros/", libro_lista, name="libros_lista"),
    path("libros/<int:id>/modificar/", actualizar_libro, name="actualizar_socio"),
    path("libros/<int:id>/changeStatus", activar_cambiar_libro, name="status_libros"),
```
- Lista

- Socio Lista

- GET /home/socios/

<p>Lista de los socios obenida desde la base de datos</p>

```python
    try:
        socios = Socio.objects.all()
        context = {"socios": socios }
        return render(request, "socio_lista.html", context)
    except Exception:
         return render(request, "socio_lista.html")
```

# Socio Registro

- Socio Nuevo

- POST /home/socios/nuevo

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

# Socio Modificar

- Socio Modificar

- PUT /home/socios/{id}/modificar

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

# Socio Eliminar

- DELETE /home/socios/{id}/eliminar

<p></p>

# __Libro Vistas__

- Lista

- Libro Lista

- GET /home/libros/

<p>Lista de los libros obenida desde la base de datos</p>

```python
    try:
        libros = Libro.objects.all()
        context = {"libros": libros }
        return render(request, "libro_lista.html", context)
    except Exception:
         return render(request, "libro_lista.html")
```

# Libro Registro

- Libro Nuevo

- POST /home/libros/nuevo

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

# Libro Modificar

- Libro Modificar

- PUT /home/libros/{id}/modificar

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

# Libro Eliminar

- DELETE /home/libro/{id}/eliminar

<p></p>

# __Prestamo Vistas__

- Lista

- Prestamo Lista

- GET /home/prestamos/

<p>Proporciona una lista de un prestamo de libros, el mismo nos trae datos desde las tabla de Socio, Emplead y libro asi como una fecha de prestamo y entrega del mismo</p>

```python
    try:
        prestamos = Prestamo.objects.all()
        context = {"prestamos": prestamos }
        return render(request, "prestamo_lista.html", context)
    except Exception:
         return render(request, "prestamo_lista.html")
```

# Prestamo Registro

- Prestamo Nuevo

- POST /home/prestamos/nuevo

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

# Prestamo Modificar

- Prestamo Modificar

- PUT /home/prestamos/{id}/modificar

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

# Prestamo Eliiminar

- DELETE /home/prestamos/{id}/eliminar

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
# Admin

El Admin permite realizar las siguientes acciones relacionadas con la gestión de usuarios:

## Gestión de Empleados

- Crear nuevos Empleados: Permite agregar nuevos Empleados al sistema especificando su nombre, apellido, numero de legajo y el campo activo aunque si no se especifica, se pondra True por defecto.
- Editar información de Empleado: Permite actualizar la información de un usuario existente como su nombre, apellido, numero de legajo y el campo.
- Eliminar Empleado: Permite eliminar empleados del sistema de forma permanente.
- Filtrar Empleados: Permite filtrar los registros de Empleado teniendo en cuenta su campo Activo

## Gestión de Autor

- Crear nuevos Autor: Permite agregar nuevos autores al sistema especificando su nombre, apellido, nacionaliodad y un boleano activo.
- Editar información de Autor: Permite actualizar la información de un usuario existente como su nombre, apellido, nacionaliodad y un boleano activo. autor.
- Eliminar Autor: Permite eliminar autores del sistema de forma permanente.
- Busqueda: Permite realizar una búsqueda en los registros mediante el titulo.
- Filtrado: Permite filtrar los registros de libros teniendo en cuenta su campo Activo

## Gestión de Libros

- Crear nuevos Libros: Permite agregar nuevos Libros al sistema especificando su titulo, descripcion, ISBN, un boleano activo y el autor que se desplegará una lista de autores perteneciente a la base de datos de la tabla Autor.
- Editar información de Libros: Permite actualizar la información de un usuario existente como su titulo, descripcion, ISBN, un boleano activo y el autor.
- Eliminar Lbros: Permite eliminar libros del sistema de forma permanente.
- Busqueda: Permite realizar una búsqueda en los registros mediante el titulo.
- Filtrado: Permite filtrar los registros de libros teniendo en cuenta su campo Activo

## Gestión de Socios

- Crear nuevos Socios: Permite agregar nuevos Libros al sistema especificando su nombre, apellido, Fecha de nacimiento y el campo activo.
- Editar información de Socios: Permite actualizar la información de un usuario existente como su nombre, apellido, Fecha de nacimiento y el campo activo..
- Eliminar Socios: Permite eliminar socios del sistema de forma permanente.
- Busqueda: Permite realizar una búsqueda en los registros mediante el nombre o el apellido.
- Filtrado: Permite filtrar los registros de libros teniendo en cuenta su campo Activo

## Gestión de Prestamos

- Crear nuevos Socios: Permite agregar nuevos Prestamos al sistema para ello se deberá seleccionar el libro, socio y el empleado (quien hace la prestacion) que esten en el sistema y que tengan el campo activo. Luego se establece la fecha de entrega y la fecha de devolucion.
- Editar información de Prestamos: Permite actualizar la información de un prestamo existente como libro, socio, empleado, fecha de entrega y fecha de devolucion
- Eliminar prestamos: Permite eliminar prestamos del sistema de forma permanente.
- Busqueda: Permite realizar una búsqueda en los registros mediante el socio, el libro o el empleado.


# API Documetancion
# Api del Sistema

## Endpoints de la API del Sistema

| Endpoint | Descripción |
| -------- | ----------- |
| [/api/libros/](#lista-de-libros)| Listado de Libros |
| [/api/libros/{id}/](#obtener-un-libro) | Obtener un Libro |
| [/api/empleados/](#lista-de-empleados)| Listado de Empleados |
| [/api/socios/](#lista-de-socios)| Listado de Socios |
| [/api/autores/](#autor-lista)| Listado de Autores |

## Lista de Libros

### URL

![Screenshot_32](https://github.com/EbanSnt/-WebApp/assets/133908306/5db7fbfe-f2bd-48e5-a8b3-752c589be709)


```python
def end_libros_todos(request):
    #TRAEMOS TODOS LOS LIBROS
    try:
        libros = Libro.objects.all().values()
        print(libros)

        #CREAMOS UNA LISTA VACIA
        libros_data =[]
        
        for libro in libros:
            #HAY QUE TENER ENCUENTA SI TRABAJAMOS CON FOREIGN KEY, DEBEMOS BUSCAR EL FK EN SU MODELO CORRESPONDIENTE

            autor = Autor.objects.get(id=libro["autor_id"])
            
            #CREAMOS UN ELEMENTO PARA AGREGARLO A LIBROS_DATA
            libro_data ={"id":libro["id"], "titulo":libro["titulo"], "autor":autor.nombre}
        
            libros_data.append(libro_data)
        
        if not libros_data:
            raise Exception("No hay libros Registrados")

        #RETORNAMO LA LISTA EN UN JSON
        return JsonResponse(libros_data,safe=False)
    except Exception as e:
        return JsonResponse({"message":str(e)})
```

## Obtener un Libro

### URL

![Screenshot_33](https://github.com/EbanSnt/-WebApp/assets/133908306/60880c99-4acb-43f0-bc4a-d2465dfbcec5)

```python
def end_libros_id(request,id):
    try:
        #TRAEMOS EL LIBRO
        libro = Libro.objects.get(id=id)
        print(libro)
        #CREAMOS UNA LISTA VACIA
        libro_data =[]
        #HAY QUE TENER ENCUENTA SI TRABAJAMOS CON FOREIGN KEY, DEBEMOS BUSCAR EL FK EN SU MODELO CORRESPONDIENTE
        autor = Autor.objects.get(id=libro.id)
        #CREAMOS UN ELEMENTO PARA AGREGARLO A LIBRO_DATA
        libro ={"id":libro.id, "titulo":libro.titulo,"descripcion":libro.descripcion,"autor":autor.nombre}

        libro_data.append(libro)
        #RETORNAMO LA LISTA EN UN JSON
        return JsonResponse(libro_data,safe=False)
    except:
        libro_data =[]
        return JsonResponse(libro_data,safe=False)
```


## Lista de Empleados

### URL

![Screenshot_34](https://github.com/EbanSnt/-WebApp/assets/133908306/fc4ff301-664e-4e70-8434-e3445708e908)

```python
def end_empleados(request):
    try:
        empleados = Empleado.objects.all()
        empleados_data = [] # creamos una lista vacia
        for empleado in empleados:
            empleado_data = { 
                "id":empleado.id, # agregamos el id del empleado
                "nombre":empleado.nombre, # agregamos el nombre del empleado
                "apellido":empleado.apellido, # agregamos el apellido del empleado
                "nlegajo":empleado.numero_legajo, # agregamos el numero de legajo del empleado
                "activo":empleado.activo, # agregamos el estado del empleado
                }
            empleados_data.append(empleado_data) # agregamos el empleado_data a la lista empleados_data
        if not empleados_data:
            raise Exception("No hay empleados registrados") # si no hay empleados registrados, levantamos una excepcion
        return JsonResponse(empleados_data,safe=False)  
    except Exception as e:
        return JsonResponse({"message":str(e)}) # retornamos el mensaje de la excepcion en un json
```

## Lista de Socios

### URL

![Screenshot_35](https://github.com/EbanSnt/-WebApp/assets/133908306/d7d7e1ac-1a38-49d4-aeae-c826ef72637f)

```python
def end_socios(request):
    try:
        socios = Socio.objects.all()
        print(socios)
        socios_data =[]
        for socio in socios:
            socio ={"id":socio.id, "nombre":socio.nombre,"apellido":socio.apellido,"fecha_nacimiento":socio.fecha_nacimiento,"activo":socio.activo}

            socios_data.append(socio)
        #RETORNAMO LA LISTA EN UN JSON
        return JsonResponse(socios_data,safe=False)
    except:
        socio_data =[]
        return JsonResponse(socio_data,safe=False)
```

## Lista de Autores

### URL

![Screenshot_36](https://github.com/EbanSnt/-WebApp/assets/133908306/b0d7c6b7-9af9-48b0-871a-e2384b319f8c)

```python
def end_autores(request):
    try:
        autores = Autor.objects.all()
        autores_data =[]
        for autor in autores:
            autor ={"id":autor.id, "nombre":autor.nombre,"apellido":autor.apellido,"nacionalidad":autor.nacionalidad,"activo":autor.activo}

            autores_data.append(autor)
        #RETORNAMO LA LISTA EN UN JSON
        return JsonResponse(autores_data,safe=False)
    except:
        socio_data =[]
        return JsonResponse(autores_data,safe=False)
```
