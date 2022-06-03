from django.contrib import admin
from apps.prestamos.models import Usuario, Ejemplar, Prestar

# Register your models here.

admin.site.register(Usuario)
admin.site.register(Ejemplar)
admin.site.register(Prestar)