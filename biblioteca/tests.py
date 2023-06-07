from datetime import datetime
from django.test import TestCase
from biblioteca.models import Autor, Empleado, Libro, Prestamo_libro, Socio


class AutoreTestCase(TestCase):

    def setUp(self):
        Autor.objects.create(nombre='Marcos', apellido='Eduardo',nacionalidad="Peru", activo=True)

    def test_autor_estado_true(self):
        autor = Autor.objects.get(nombre='Marcos')
        self.assertEqual(autor.activo, True)
    
    def test_autor_estado_false(self):
        autor = Autor.objects.get(nombre='Marcos')
        self.assertEqual(autor.activo, True)
    
    def test_autor_nombre(self):
        autor = Autor.objects.get(nombre='Marcos')
        self.assertEqual(autor.nombre, "Marcos")
    
    def test_autor_apellido(self):
        autor = Autor.objects.get(nombre='Marcos')
        self.assertEqual(autor.apellido, "Eduardo")
    
    def test_autor_nacionalidad(self):
        autor = Autor.objects.get(nombre='Marcos')
        self.assertEqual(autor.nacionalidad, "Chile")
    




class LibroAutorTestCase(TestCase):

    def setUp(self):
        Autor.objects.create(nombre='Marcos', apellido='Eduardo',nacionalidad="Chile", activo=True)
        Libro.objects.create(titulo='El señor de los anillos',isbn="9784561237895" , autor=Autor.objects.get(nombre='Marcos'), activo=True)
    
    def test_libro_autor(self):
        libro = Libro.objects.get(titulo='El señor de los anillos')
        self.assertEqual(libro.autor.nombre, "Marcos")
    
    def test_libro_titulo(self):
        libro = Libro.objects.get(titulo='El señor de los anillos')
        self.assertEqual(libro.titulo, "El señor de los anillos")
    
    def test_autor_nombre(self):
        autor = Autor.objects.get(nombre='Marcos')
        self.assertEqual(autor.nombre, "Marcos")
    
    def test_autor_apellido(self):
        autor = Autor.objects.get(nombre='Marcos')
        self.assertEqual(autor.apellido, "Eduardo")
    


class EmpleadoTestCase(TestCase):

    def setUp(self):
        Empleado.objects.create(nombre='Marcos', apellido='Eduardo', numero_legajo='12345678', activo=True)

    def test_empleado_estado_true(self):
        emp = Empleado.objects.get(nombre='Marcos')
        self.assertEqual(emp.activo, True)

    def test_empleado_estado_false(self):
        emp = Empleado.objects.get(nombre='Marcos')
        self.assertEqual(emp.activo, True)
    
    def test_empleado_legajo(self):
        emp = Empleado.objects.get(nombre='Marcos')
        self.assertEqual(emp.numero_legajo, "12345678")
    
    def test_empleado_nombre(self):
        emp = Empleado.objects.get(nombre='Marcos')
        self.assertEqual(emp.nombre, "Marcos")
    
    def test_empleado_apellido(self):
        emp = Empleado.objects.get(nombre='Marcos')
        self.assertEqual(emp.apellido, "Eduardo")
    


class SocioTestCase(TestCase):

    def setUp(self):
        Socio.objects.create(nombre="Marcos", apellido="Eduardo", fecha_nacimiento= datetime.strptime("2009-01-01", "%Y-%m-%d").date(), activo=True)

    
    def test_socio_nombre(self):
        soc = Socio.objects.get(nombre="Marcos")
        self.assertEqual(soc.nombre, "Marcos")

    def test_socio_apellido(self):
        soc = Socio.objects.get(nombre="Marcos")
        self.assertEqual(soc.apellido, "Eduardo")
    
    def test_socio_fecha_nacimiento(self):
        soc = Socio.objects.get(nombre="Marcos")
        fecha_nacimiento = datetime.strptime("2009-01-01", "%Y-%m-%d").date()
        self.assertEqual(soc.fecha_nacimiento, fecha_nacimiento)
    
    def test_socio_activo(self):
        soc = Socio.objects.get(nombre="Marcos")
        self.assertEqual(soc.activo, True)
    


class PrestamoTestCase(TestCase):

    def setUp(self):
        Socio.objects.create(nombre="Marcos", apellido="Eduardo", fecha_nacimiento= datetime.strptime("2009-01-01", "%Y-%m-%d").date(), activo=True)
        Empleado.objects.create(nombre='Marcos', apellido='Eduardo', numero_legajo='12345678', activo=True)
        Autor.objects.create(nombre='Marcos', apellido='Eduardo',nacionalidad="Chile", activo=True)
        Libro.objects.create(titulo='El señor de los anillos',isbn="9784561237895" , autor=Autor.objects.get(nombre='Marcos'), activo=True)
        Prestamo_libro.objects.create(socio=Socio.objects.get(nombre="Marcos"), empleado=Empleado.objects.get(nombre='Marcos'), libro=Libro.objects.get(titulo='El señor de los anillos'), fecha_prestamo=datetime.strptime("2021-01-01", "%Y-%m-%d").date(), fecha_devolucion=datetime.strptime("2021-01-01", "%Y-%m-%d").date())

    def test_prestamo_socio(self):
        prestamo = Prestamo_libro.objects.get(socio=Socio.objects.get(nombre="Marcos"))
        self.assertEqual(prestamo.socio.nombre, "Marcos")
    
    def test_prestamo_empleado(self):
        prestamo = Prestamo_libro.objects.get(empleado=Empleado.objects.get(nombre='Marcos'))
        self.assertEqual(prestamo.empleado.nombre, "Marcos")
    
    def test_prestamo_libro(self):
        prestamo = Prestamo_libro.objects.get(libro=Libro.objects.get(titulo='El señor de los anillos'))
        self.assertEqual(prestamo.libro.titulo, "El señor de los anillos")
    
    def test_prestamo_fecha_prestamo(self):
        prestamo = Prestamo_libro.objects.get(fecha_prestamo=datetime.strptime("2021-01-01", "%Y-%m-%d").date())
        self.assertEqual(prestamo.fecha_prestamo, datetime.strptime("2021-01-01", "%Y-%m-%d").date())
    
    def test_prestamo_fecha_devolucion(self):
        prestamo = Prestamo_libro.objects.get(fecha_devolucion=datetime.strptime("2021-01-01", "%Y-%m-%d").date())
        self.assertEqual(prestamo.fecha_devolucion, datetime.strptime("2021-01-01", "%Y-%m-%d").date())

