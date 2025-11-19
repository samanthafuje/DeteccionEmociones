from django.db import models

# Modelo Alumno
class alumno(models.Model):
    id_alumno = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30, help_text="Ingrese tu nombre")
    apellido_parterno = models.CharField(max_length=20, help_text="Apellido paterno")
    apellido_materno = models.CharField(max_length=20, help_text="Apellido materno")
    edad = models.PositiveIntegerField()
    licenciatura = models.CharField(max_length=40)
    aprendizaje = [
        ('visual', 'Visual'),
        ('auditivo', 'Auditivo'),
        ('kinestesico', 'Kinestésico'),
        ]
    tipo_aprendizaje = models.CharField(max_length=20, choices=aprendizaje, default='visual')
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

class estilos_aprendizaje(models.Model):
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
    
    resultado =models.CharField(max_length=50,blank=True)
    
    def __str__(self):
        return f"Resultado: {self.alumno.nombre} {self.resultado}"


#usuario
class usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nombre = models.CharField (max_length=50)
    rool = models.CharField(max_length=20)
def __self__(self):
    return f"{self.nombre} {self.rool}"

#emocion
class emocion(models.Model):
    id_emocion = models.AutoField(primary_key=True)
    emocion = models.CharField(max_length=45)

#Reporte
class reporte(models.Model):
    id_reporte = models.AutoField(primary_key=True)
    Resultado = models.CharField(max_length=45)
    id_emocion = models.ForeignKey(emocion, on_delete=models.CASCADE)
    id_alumno = models.ForeignKey(alumno, on_delete=models.CASCADE)
def __self__(self):
    return f"{self.id_alumno} {self.id_emocion}"

#Texto
class texto(models.Model):
    id_texto = models.AutoField(primary_key=True)
    contenido = models.CharField(max_length=1000)
    id_emocion = models.ForeignKey(emocion, on_delete=models.CASCADE)

#Diccionario
class diccionario(models.Model):
    id_palabras = models.AutoField(primary_key=True)
    id_emocion = models.ForeignKey(emocion, on_delete=models.CASCADE)
    palabra = models.CharField(max_length=10)
    
