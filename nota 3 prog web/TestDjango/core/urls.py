from django.urls import path
from .views import menu, acercade, carrousel, formulario, galeria, login_view, django_view, eliminar, modificar

urlpatterns = [
    path('', menu, name='menu'),          # Ruta para la vista del menú (Página principal)
    path('acercade/', acercade, name='acercade'),  # Ruta para la vista de "acerca de"
    path('carrousel/', carrousel, name='carrousel'),  # Ruta para el carrusel
    path('formulario/', formulario, name='formulario'),  # Ruta para el formulario
    path('galeria/', galeria, name='galeria'),  # Ruta para la galería
    path('login/', login_view, name='login'),  # Ruta para el login
    path('django/', django_view, name='django' ),
    path('modificar/', modificar, name='modificar' ),
    path('eliminar/<id>', eliminar, name='eliminar' ),
    path('modificar/<int:id>/', modificar, name='modificar' )
]
