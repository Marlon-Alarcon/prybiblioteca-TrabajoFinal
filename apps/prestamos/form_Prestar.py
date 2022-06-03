from django import forms
from apps.prestamos.models import Prestar

class PrestarForm(forms.ModelForm):
    class Meta:
        model = Prestar
        #Es una lista
        fields = [
            'fechadev',
            'fechapres',
            'usuario',
            'ejemplar',
        ]
        #Es un objeto y pongo llave: valor
        labels = {
            'fechadev': 'Ingrese la fecha de devolucion',
            'fechapres': 'Ingrese la fecha de prestamo',
            'usuario': 'Seleccione el Usuario',
            'ejemplar': 'Seleccione el Ejemplar',
        }

        widgets ={
            'fechadev': forms.TextInput(attrs={'class': 'form-control'}),
            'fechapres': forms.TextInput(attrs={'class': 'form-control'}),
            'usuario': forms.Select(attrs={'class': 'form-control'}),
            'ejemplar': forms.Select(attrs={'class': 'form-control'}),
        }