from django import forms
from catalog.models import alumno
from catalog.models import EstilosAprendizaje

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
        model = EstilosAprendizaje
        fields = [
            'alumno','p1','p2','p3','p4','p5','p6','p7','p8','p9','p10'
        ]
        
        widgets = {
            'alumno': forms.Select(),
            'p1': forms.RadioSelect(choices=OPCIONES),
            'p2': forms.RadioSelect(choices=OPCIONES),
            'p3': forms.RadioSelect(choices=OPCIONES),
            'p4': forms.RadioSelect(choices=OPCIONES),
            'p5': forms.RadioSelect(choices=OPCIONES),
            'p6': forms.RadioSelect(choices=OPCIONES),
            'p7': forms.RadioSelect(choices=OPCIONES),
            'p8': forms.RadioSelect(choices=OPCIONES),
            'p9': forms.RadioSelect(choices=OPCIONES),
            'p10': forms.RadioSelect(choices=OPCIONES),
        }
        
        widgets['alumno'] = forms.Select()