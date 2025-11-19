from django import forms
from catalog.models import alumno
from catalog.models import estilos_aprendizaje

class AlumnoForm(forms.ModelForm):
    class Meta:
        model = alumno
        fields = '__all__'

OPCIONES = [
    ('A', 'A (Siempre)'),
    ('B', 'B (A veces)'),
    ('C', 'C (Nunca)'),
]

class estilos_aprendizajeForm(forms.ModelForm):
    class Meta:
        model = estilos_aprendizaje
        fields = [
            'alumno','p1','p2','p3','p4','p5','p6','p7','p8','p9','p10'
        ]
        
        widgets = {
            field: forms.RadioSelect(choices=OPCIONES)
            for field in fields if field != 'alumno'
        }
        
        widgets['alumno'] = forms.Select()