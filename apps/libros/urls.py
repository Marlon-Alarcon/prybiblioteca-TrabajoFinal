from django.urls import path
from apps.libros.views import listLibros,LibroCreate, LibroEdit, libroElim, listAutores, AutorCreate, AutorEdit,AutorElim

app_name='libros'
urlpatterns = [
    path('', listLibros, name='listLibros'),
    path('nuevo/', LibroCreate, name='LibroCreate'),
    path('actualizar/<int:id_libro>/', LibroEdit, name='LibroEdit'),
    path('Eliminar/<int:id_libro>/', libroElim, name='libroElim'),

    #----------------------
    #----- AUTORES --------
    #----------------------

    path('AutorL', listAutores, name='listAutores'),
    path('nuevo-Autor/', AutorCreate, name='AutorCreate'),
    path('act-Autor/<int:id_autor>/', AutorEdit, name='AutorEdit'),
    path('Elim-Autor/<int:id_autor>/', AutorElim, name='AutorElim'),
]