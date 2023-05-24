from django.test import TestCase
from .models import * 

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
        self.assertEqual(response.status_code, 200)

        #ACA SE OBTIENE UN FILTER SOBRE LO QUE PUSISTE Y LO GUARDA
        autor_db= Autor.objects.filter(nombre ="Adrian", apellido="Rodriguez",nacionalidad="Argentino", activo=True)
        
        #ACA SE TESTEA SI HAY ALGO EN LA VARIABLE ANTERIOR, SI ES 0 FALLA
        self.assertEqual(autor_db.count(),1)

