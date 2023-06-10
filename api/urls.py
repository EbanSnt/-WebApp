
from django.urls import include, path
from .views import *
from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'libros', LibroViewSet)
router.register(r'empleados', EmpleadoViewSet)
router.register(r'socios', SocioViewSet)
router.register(r'autores', AutorViewSet)
router.register(r'prestamos', Prestamo_libroViewSet)

urlpatterns =[
    
    path('', include(router.urls))
]