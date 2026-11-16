from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator


class Estudiante(models.Model):

    usuario = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='estudiante'
    )

    nombre = models.CharField(max_length=100)
    apellido_paterno = models.CharField(max_length=100)
    apellido_materno = models.CharField(max_length=100)
    edad = models.PositiveIntegerField()
    licenciatura = models.CharField(max_length=150)
    correo = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido_paterno}"


class RespuestaEstilo(models.Model):

    estudiante = models.ForeignKey(
        Estudiante,
        on_delete=models.CASCADE,
        related_name='respuestas_estilo'
    )

    pregunta = models.PositiveIntegerField()

    respuesta = models.CharField(
        max_length=10
    )

    fecha = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['estudiante', 'pregunta'],
                name='unique_respuesta_estudiante_pregunta'
            )
        ]

    def __str__(self):
        return f"{self.estudiante} - Pregunta {self.pregunta}"


class ResultadoEstilo(models.Model):

    estudiante = models.OneToOneField(
        Estudiante,
        on_delete=models.CASCADE,
        related_name='resultado_estilo'
    )

    activo = models.PositiveIntegerField(default=0)
    reflexivo = models.PositiveIntegerField(default=0)
    teorico = models.PositiveIntegerField(default=0)
    pragmatico = models.PositiveIntegerField(default=0)

    estilo_predominante = models.CharField(
        max_length=20,
        blank=True
    )

    fecha = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return f"{self.estudiante} - {self.estilo_predominante}"

from django.db import models


class EvaluacionDASS21(models.Model):

    estudiante = models.ForeignKey(
        'usuarios.Estudiante',
        on_delete=models.CASCADE,
        related_name='evaluaciones_dass21'
    )

    fecha = models.DateTimeField(auto_now_add=True)

    # Puntuaciones ajustadas (subtotal x 2)
    depresion = models.PositiveSmallIntegerField(default=0)
    ansiedad = models.PositiveSmallIntegerField(default=0)
    estres = models.PositiveSmallIntegerField(default=0)

    # Interpretaciones
    nivel_depresion = models.CharField(max_length=30)
    nivel_ansiedad = models.CharField(max_length=30)
    nivel_estres = models.CharField(max_length=30)

    def __str__(self):
        return f"DASS-21 - {self.estudiante} - {self.fecha}"


class RespuestaDASS21(models.Model):

    evaluacion = models.ForeignKey(
        EvaluacionDASS21,
        on_delete=models.CASCADE,
        related_name='respuestas'
    )

    pregunta = models.PositiveSmallIntegerField()

    respuesta = models.PositiveSmallIntegerField(
        choices=[
            (0, 'No me ha ocurrido'),
            (1, 'Me ha ocurrido un poco'),
            (2, 'Me ha ocurrido bastante'),
            (3, 'Me ha ocurrido mucho'),
        ]
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['evaluacion', 'pregunta'],
                name='respuesta_dass21_unica'
            )
        ]

    def __str__(self):
        return f"Pregunta {self.pregunta}: {self.respuesta}"




class TextoEstudiante(models.Model):
    estudiante = models.ForeignKey(
        'usuarios.Estudiante',
        on_delete=models.CASCADE,
        related_name='textos'
    )

    contenido = models.TextField(
        validators=[MinLengthValidator(30)]
    )

    fecha_creacion = models.DateTimeField(auto_now_add=True)

    procesado = models.BooleanField(default=False)

    class Meta:
        ordering = ['-fecha_creacion']
        verbose_name = 'Texto del estudiante'
        verbose_name_plural = 'Textos de estudiantes'

    def __str__(self):
        return f'Texto de {self.estudiante} - {self.fecha_creacion:%d/%m/%Y}'


class AnalisisTexto(models.Model):

    texto = models.OneToOneField(
        TextoEstudiante,
        on_delete=models.CASCADE,
        related_name='analisis'
    )

    total_palabras = models.PositiveIntegerField(default=0)

    indicadores_detectados = models.JSONField(default=dict, blank=True)

    version_procesamiento = models.CharField(
        max_length=30,
        default='prototipo-1.0'
    )

    fecha_analisis = models.DateTimeField(auto_now=True)

    estado = models.CharField(
        max_length=20,
        default='pendiente'
    )

    def __str__(self):
        return f'Análisis del texto {self.texto_id}'
