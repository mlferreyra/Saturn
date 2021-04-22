from django import forms
from django.contrib.auth.forms import UserCreationForm

from users.models import Registro

class RegistroForm(UserCreationForm):
    
    class Meta:
        model = Registro
        fields = [
            "email",
            "password1",
            "password2",
            "nombre",
            "apellido",
            "dni",
            "telefono",
            "fechaDeNacimiento",
            "sexo"
        ]
        label = {
            'email': 'Email',
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'dni': 'Ingrese su DNI',
            'telefono': 'Telefono',
            'fechaDeNacimiento': 'Fecha de Nacimiento',
            'sexo': 'Sexo'
        }
        widgets = {
            'email': forms.TextInput(attrs={'class': 'form-control', 'type': 'email'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'dni': forms.NumberInput(attrs={'class': 'form-control'}),
            'telefono': forms.NumberInput(attrs={'class': 'form-control'}),
            'fechaDeNacimiento': forms.DateInput(attrs={'class': 'form-control', 'type':'date'}),
            'sexo': forms.RadioSelect(attrs={'class':'form-check-input mb-3 mt-2'})
        }
        
