from django.urls import path
from apps.prestamos.views import listPrestamos, PrestarCreate, PrestarEdit, PrestarElim, listUsuarios,UsuarioCreate,UsuarioEdit ,UsuarioElim, listEjemplares, EjemplarCreate, EjemplarEdit, EjemplarElim, consulta1, consulta2, consulta3

app_name='prestamos'
urlpatterns = [
    path('', listPrestamos, name='listPrestamos'),
    path('nuevo/', PrestarCreate, name='PrestarCreate'),
    path('actualizar/<int:id_prestar>/', PrestarEdit, name='PrestarEdit'),
    path('eliminar/<int:id_prestar>/', PrestarElim, name='PrestarElim'),


    path('Usuario', listUsuarios, name='listUsuarios'),
    path('new-Usuario/', UsuarioCreate, name='UsuarioCreate'),
    path('act-Usuario/<int:id_usuario>/', UsuarioEdit, name='UsuarioEdit'),
    path('elim-Usuario/<int:id_usuario>/', UsuarioElim, name='UsuarioElim'),


    path('Ejemplares', listEjemplares, name='listEjemplares'),
    path('new-Ejemplares/', EjemplarCreate, name='EjemplarCreate'),
    path('act-Ejemplares/<int:id_ejemplar>/', EjemplarEdit, name='EjemplarEdit'),
    path('elim-Ejemplares/<int:id_ejemplar>/', EjemplarElim, name='EjemplarElim'),

    path('Consulta1', consulta1, name='consulta1'),
    path('Consulta2', consulta2, name='consulta2'),
    path('consulta3', consulta3, name='consulta3'),
]