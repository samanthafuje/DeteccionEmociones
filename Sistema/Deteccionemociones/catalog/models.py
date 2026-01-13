from django.db import models

# Modelo Alumno
class alumno(models.Model):
    id_alumno = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30, help_text="Ingrese tu nombre")
    apellido_parterno = models.CharField(max_length=20, help_text="Apellido paterno")
    apellido_materno = models.CharField(max_length=20, help_text="Apellido materno")
    edad = models.PositiveIntegerField()
    licenciatura = models.CharField(max_length=40)
    correo = models.EmailField(max_length=40, blank=True, null=True)
    aprendizaje = [
        ('visual', 'Visual'),
        ('auditivo', 'Auditivo'),
        ('kinestesico', 'Kinestésico'),
        ]
    tipo_aprendizaje = models.CharField(max_length=20, blank=True, null=True)
    def __str__(self):
        return f"{self.nombre} {self.apellido_parterno} {self.apellido_materno}"


#Modelo Test

class test(models.Model):
    id_test = models.AutoField(primary_key=True)
    emocion = models.CharField(max_length=30)
    texto_generado = models.CharField(max_length=1000)

def __self__(self):
    return f"{self.Emocion} {self.Texto_generado}"

#Modelo Tipos de Aprendizaje

class EstilosAprendizaje(models.Model):
    alumno = models.ForeignKey(alumno, on_delete=models.CASCADE)
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

    def __str__(self):
        return f"Resultado: {self.alumno.nombre} → {self.resultado}"


class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    rol = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.nombre} ({self.rol})"


class Emocion(models.Model):
    emocion = models.CharField(max_length=45)

    def __str__(self):
        return self.emocion


class Reporte(models.Model):
    resultado = models.CharField(max_length=45)
    emocion = models.ForeignKey(Emocion, on_delete=models.CASCADE)
    alumno = models.ForeignKey(alumno, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.alumno} → {self.emocion}"


class Texto(models.Model):
    contenido = models.CharField(max_length=1000)
    emocion = models.ForeignKey(Emocion, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.emocion}: {self.contenido[:40]}"


class Diccionario(models.Model):
    emocion = models.ForeignKey(Emocion, on_delete=models.CASCADE)
    palabra = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.palabra} ({self.emocion})"