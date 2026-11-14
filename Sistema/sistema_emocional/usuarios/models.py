from django.db import models
from django.contrib.auth.models import User


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