from django.db import models

# Create your models here.
class Proyecto(models.Model):
    nombre = models.CharField( max_length=40)
    codigo = models.IntegerField()

class ProjectManager(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email=models.CharField(max_length=50)

opciones = [
    ('opcion1', 'Sin Iniciar'),
    ('opcion2', 'Iniciada'),
    ('opcion3', 'Terminada'),
]
class Tareas(models.Model):
    nombreTarea = models.CharField( max_length=50, blank=False )
    fechaInicio=models.DateField()
    fechaTermino=models.DateField()
    estado=models.CharField(max_length=20, choices=opciones)
