from django.db import models
from apps.libros.models import Libro

# Create your models here.

class Usuario(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=15)
    direccion = models.CharField(max_length=20)
    telefono = models.CharField(max_length=10)

    def __str__(self):
        return str(self.nombre)


class Ejemplar(models.Model):
    localizacion = models.CharField(max_length=15)
    libro = models.ForeignKey(Libro, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.localizacion)


class Prestar(models.Model):
    fechadev = models.DateField()
    fechapres = models.DateField()
    usuario = models.ForeignKey(Usuario, null=True, blank=True, on_delete=models.CASCADE)
    ejemplar = models.ForeignKey(Ejemplar, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.fechapres)