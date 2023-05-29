from django.test import TestCase
from .models import * 
from django.urls import reverse

# Create your tests here.
"""
TEST AUTOR
BEGIN HERE
"""
class AutorNuevoTest(TestCase):
    def test_agregar_autores(self):
        #IMPORTANTE! USAR EL FORMATO /api/el_resto_del_ur/ QUE DESEAS PROBAR, SINO NO FUNCIONA
        response = self.client.post("/api/autores/nuevo/",{"nombre":"Adrian","apellido":"Rodriguez","nacionalidad":"Argentino","activo":True})
        
        #ACÁ SE TESTEA SI SE PUEDO HACER EL POST, SI SALE 404, ENTONCES ESTA MAL EL URL
        self.assertEqual(response.status_code, 302)

        #ACA SE OBTIENE UN FILTER SOBRE LO QUE PUSISTE Y LO GUARDA
        autor_db= Autor.objects.filter(nombre ="Adrian", apellido="Rodriguez",nacionalidad="Argentino", activo=True)
        
        #ACA SE TESTEA SI HAY ALGO EN LA VARIABLE ANTERIOR, SI ES 0 FALLA
        self.assertEqual(autor_db.count(),1)

    def test_changestatus_autores(self):
       #PROBAR QUE LA VIEW QUE CAMBIAR AUTOR.ACTIVO DE FALSE A TRUE Y VICEVERSA 
       #FUNCIONE DE MANERA CORRECTA
       
       newAutor =Autor.objects.create(nombre="Juan", apellido="Pérez", nacionalidad="Argentino", activo=False)
       
       url = reverse("activar_autor", kwargs={"id":newAutor.id})
       
       response = self.client.post(url)
       
       autorChange = Autor.objects.get(id=newAutor.id)
       
       self.assertTrue(autorChange.activo)
       
       # DEBIDO A QUE NO HACE FALTA UN TEMPLATE, EL CODIGO SERA 302 YA QUE ES UN REDIRECCIONAMIENTO A LA LISTA AUTORES
       self.assertEqual(response.status_code,302)

    def test_show_Autores(self):
        #TEST PARA VER SI SE RENDERIZA EL TITULO DEL TEMPLATE UTILIZADO

        response = self.client.get("/api/autores/")
        self.assertContains(response, "Lista de Autores")

    def test_actualizar_autor(self):
        #TEST PARA VER SI FUNCIONA EL FORM
        newAutor =Autor.objects.create(nombre="Juan", apellido="Pérez", nacionalidad="Argentino", activo=False)

        url = reverse("actualizar_autor",kwargs={"id":newAutor.id})
        
        response = self.client.post(url,{"nombre":"Javier","apellido":"Pérez", "nacionalidad":"Argentino", "activo":False})
        
        self.assertEqual(response.status_code,302)
        
        autor_db= Autor.objects.filter(nombre ="Javier", apellido="Pérez",nacionalidad="Argentino", activo=True)

        self.assertEqual(autor_db.count(),1)