from django import forms
from apps.prestamos.models import Usuario

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        #Es una lista
        fields = [
            'nombre',
            'apellido',
            'direccion',
            'telefono',
        ]
        #Es un objeto y pongo llave: valor
        labels = {
            'nombre': 'Ingrese el nombre',
            'apellido': 'Ingrese el apellido',
            'direccion': 'Ingrese la direccion',
            'telefono': 'Ingrese el telefono',
        }

        widgets ={
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
        }