from django import forms
from apps.libros.models import Autor

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        #Es una lista
        fields = [
            'nombre',

        ]
        #Es un objeto y pongo llave: valor
        labels = {
            'nombre': 'Ingrese el nombre del Autor',
        }

        widgets ={
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
        }