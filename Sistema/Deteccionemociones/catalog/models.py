from django.db import models

class alumno(models.Model):
    id_alumno = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)
    apellido_paterno = models.CharField(max_length=20)
    apellido_materno = models.CharField(max_length=20)
    edad = models.PositiveIntegerField()
    licenciatura = models.CharField(max_length=40)

    tipo_aprendizaje = models.CharField(
        max_length=20,
        blank=True,
        null=True
    )

    def __str__(self):
        return f"{self.nombre} {self.apellido_paterno} {self.apellido_materno}"
    
class estilos_aprendizaje(models.Model):
    alumno = models.ForeignKey(alumno, on_delete=models.CASCADE, related_name='estilosaprendizaje')
    p1 = models.CharField(max_length=1)
    p2 = models.CharField(max_length=1)
    p3 = models.CharField(max_length=1)
    p4 = models.CharField(max_length=1)
    p5 = models.CharField(max_length=1)
    p6 = models.CharField(max_length=1)
    p7 = models.CharField(max_length=1)
    p8 = models.CharField(max_length=1)
    p9 = models.CharField(max_length=1)
    p10 = models.CharField(max_length=1)

    resultado = models.CharField(max_length=50, blank=True)
  
