from django import forms
from .models import Estudiante


class EstudianteForm(forms.ModelForm):

    password = forms.CharField(
        label='Contraseña',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Contraseña'
        }),
        min_length=8
    )

    class Meta:
        model = Estudiante

        fields = [
            'nombre',
            'apellido_paterno',
            'apellido_materno',
            'edad',
            'licenciatura',
            'correo'
        ]

        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre'
            }),

            'apellido_paterno': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Apellido paterno'
            }),

            'apellido_materno': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Apellido materno'
            }),

            'edad': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Edad',
                'min': 19,
                'max': 25
            }),

            'licenciatura': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Licenciatura'
            }),

            'correo': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Correo electrónico'
            }),
        }