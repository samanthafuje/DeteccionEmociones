from django.contrib import admin
from .models import AnalisisTexto
from .models import (
    Estudiante,
    RespuestaEstilo,
    EvaluacionDASS21,
    RespuestaDASS21,
    TextoEstudiante
)

admin.site.register(Estudiante)
admin.site.register(RespuestaEstilo)
admin.site.register(EvaluacionDASS21)
admin.site.register(RespuestaDASS21)
admin.site.register(TextoEstudiante)
admin.site.register(AnalisisTexto)