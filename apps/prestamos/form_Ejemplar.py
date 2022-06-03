from django import forms
from apps.prestamos.models import Ejemplar

class EjemplarForm(forms.ModelForm):
    class Meta:
        model = Ejemplar
        #Es una lista
        fields = [
            'localizacion',
            'libro',
        ]
        #Es un objeto y pongo llave: valor
        labels = {
            'localizacion': 'Ingrese la localizacion',
            'libro': 'Seleccione el Libro',
        }

        widgets ={
            'localizacion': forms.TextInput(attrs={'class': 'form-control'}),
            'libro': forms.Select(attrs={'class': 'form-control'}),
        }