from django.db import models

# Create your models here.
class Proyecto(models.Model):
    nombre = models.CharField( max_length=40)
    codigo = models.IntegerField()
    
    def __str__(self):
        return f'{self.nombre} - {self.codigo}'

class ProjectManager(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    def __str__(self):
        return f'{self.nombre} {self.apellido}'

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
    def __str__(self):
        return f'{self.nombreTarea}'
