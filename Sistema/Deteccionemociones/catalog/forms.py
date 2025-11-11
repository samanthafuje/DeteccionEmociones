from django import forms
from catalog.models import alumno

class AlumnoForm(forms.ModelForm):
    class Meta:
        model = alumno
        fields = '__all__'
