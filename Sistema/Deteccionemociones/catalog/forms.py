
from django import forms
from .models import alumno, estilos_aprendizaje

class AlumnoForm(forms.ModelForm):
    class Meta:
        model = alumno
        fields = [
            'nombre',
            'apellido_paterno',
            'apellido_materno',
            'edad',
            'licenciatura'
        ]
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido_paterno': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido_materno': forms.TextInput(attrs={'class': 'form-control'}),
            'edad': forms.NumberInput(attrs={'class': 'form-control'}),
            'licenciatura': forms.TextInput(attrs={'class': 'form-control'}),
        }
OPCIONES = [
    ('A', 'Visual'),
    ('B', 'Auditivo'),
    ('C', 'Kinestésico'),
]
class EstilosAprendizajeForm(forms.ModelForm):
    class Meta:
        model = estilos_aprendizaje
        fields = [
            'p1', 'p2', 'p3', 'p4', 'p5',
            'p6', 'p7', 'p8', 'p9', 'p10'
        ]

    p1 = forms.ChoiceField(
        label="1. Cuando estudias un tema nuevo, prefieres:",
        choices=OPCIONES,
        widget=forms.RadioSelect
    )

    p2 = forms.ChoiceField(
        label="2. Cuando alguien te da instrucciones, entiendes mejor si:",
        choices=OPCIONES,
        widget=forms.RadioSelect
    )

    p3 = forms.ChoiceField(
        label="3. En clase, te concentras más cuando:",
        choices=OPCIONES,
        widget=forms.RadioSelect
    )

    p4 = forms.ChoiceField(
        label="4. Cuando recuerdas información, normalmente lo haces:",
        choices=OPCIONES,
        widget=forms.RadioSelect
    )

    p5 = forms.ChoiceField(
        label="5. Para aprender algo nuevo, prefieres:",
        choices=OPCIONES,
        widget=forms.RadioSelect
    )

    p6 = forms.ChoiceField(
        label="6. Cuando usas una herramienta o tecnología nueva:",
        choices=OPCIONES,
        widget=forms.RadioSelect
    )

    p7 = forms.ChoiceField(
        label="7. Cuando estudias para un examen, normalmente:",
        choices=OPCIONES,
        widget=forms.RadioSelect
    )

    p8 = forms.ChoiceField(
        label="8. Cuando te cuentan una historia o un tema:",
        choices=OPCIONES,
        widget=forms.RadioSelect
    )

    p9 = forms.ChoiceField(
        label="9. Cuando trabajas en equipo, prefieres:",
        choices=OPCIONES,
        widget=forms.RadioSelect
    )

    p10 = forms.ChoiceField(
        label="10. Te resulta más fácil recordar:",
        choices=OPCIONES,
        widget=forms.RadioSelect
    )
