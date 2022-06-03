from django.db import models

# Create your models here.

class Autor(models.Model):
    nombre = models.CharField(max_length=20)

    def __str__(self):
        return str(self.nombre)


class Libro(models.Model):
    titulo = models.CharField(max_length=25)
    numeropag = models.CharField(max_length=10)
    editorial = models.CharField(max_length=20)
    isbn = models.CharField(max_length=25)
    autor = models.ManyToManyField(Autor)

    def __str__(self):
        return str(self.titulo)