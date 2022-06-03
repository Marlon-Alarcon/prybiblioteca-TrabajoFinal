from django import forms
from apps.libros.models import Libro

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        #Es una lista
        fields = [
            'titulo',
            'numeropag',
            'editorial',
            'isbn',
            'autor',
        ]
        #Es un objeto y pongo llave: valor
        labels = {
            'titulo': 'Ingrese el titulo',
            'numeropag': 'Ingrese el numero de paginas',
            'editorial': 'Ingrese la Editorial',
            'isbn': 'Ingrese el ISBN',
            'autor': 'Seleccione el autor',
        }

        widgets ={
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'numeropag': forms.TextInput(attrs={'class': 'form-control'}),
            'editorial': forms.TextInput(attrs={'class': 'form-control'}),
            'isbn': forms.TextInput(attrs={'class': 'form-control'}),
            'autor': forms.CheckboxSelectMultiple,
        }