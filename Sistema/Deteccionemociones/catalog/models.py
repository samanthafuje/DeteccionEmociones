from django.db import models

# Modelo Alumno
class Alumno(models.Model):
    id_alumno = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=30, help_text="Ingrese tú nombre")
    Apellido_parterno = models.CharField(max_length=20, help_text="Apellido paterno")
    Apellido_materno = models.CharField(max_length=20, help_text="Apellido materno")
    Edad= models.PositiveIntegerField()
    Licenciatura= models.CharField(max_length=40)
def __self__(self):
    return f"{self.nombre} {self.Apellido_parterno} {self.Apellido_materno} {self.Edad} {self.Licenciatura}"

#Modelo Test

class Test(models.Model):
    id_test = models.AutoField(primary_key=True)
    Emocion = models.CharField(max_length=30)
    Texto_generado = models.CharField(max_length=1000)

def __self__(self):
    return f"{self.Emocion} {self.Texto_generado}"