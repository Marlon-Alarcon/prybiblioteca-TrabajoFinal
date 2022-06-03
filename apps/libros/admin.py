from django.contrib import admin
from apps.libros.models import Libro,Autor

# Register your models here.

admin.site.register(Libro)
admin.site.register(Autor)