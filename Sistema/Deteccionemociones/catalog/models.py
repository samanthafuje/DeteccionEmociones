from django.db import models

# Modelo Alumno
class alumno(models.Model):
    id_alumno = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30, help_text="Ingrese tú nombre")
    apellido_parterno = models.CharField(max_length=20, help_text="Apellido paterno")
    apellido_materno = models.CharField(max_length=20, help_text="Apellido materno")
    edad= models.PositiveIntegerField()
    licenciatura= models.CharField(max_length=40)
def __self__(self):
    return f"{self.nombre} {self.apellido_parterno} {self.apellido_materno} {self.edad} {self.licenciatura}"


#Modelo Test

class test(models.Model):
    id_test = models.AutoField(primary_key=True)
    emocion = models.CharField(max_length=30)
    texto_generado = models.CharField(max_length=1000)

def __self__(self):
    return f"{self.Emocion} {self.Texto_generado}"

#Modelo Tipos de Aprendizaje

class aprendizaje(models.Model):
    id_aprendizaje = models.AutoField(primary_key=True)
    id_alumno = models.ForeignKey(alumno, on_delete=models.CASCADE)
    tipos_aprendizaje = models.CharField(max_length=40)

def __self__(self):
    return f"{self.tipos_aprendizaje}"


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