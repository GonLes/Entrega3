from django.db import models

# Create your models here.
class Proyecto(models.Model):
    nombre = models.CharField( max_length=40)
    codigo = models.IntegerField()

class ProjectManager(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email=models.CharField(max_length=50)
