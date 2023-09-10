from django.shortcuts import render
from django.http import HttpResponse
from .models import Proyecto
from .models import ProjectManager
from .models import Tareas
# Create your views here.
def proyecto(req, nombre, codigo):
    proyecto=Proyecto(nombre=nombre,codigo=codigo)
    proyecto.save()
    return HttpResponse (f"""
    <p> Proyecto:{proyecto.nombre} con codigo {proyecto.codigo} ha sido creado)""")

def projectManager(req, nombre, apellido,email):
    projectManager=ProjectManager(nombre=nombre,apellido=apellido,email=email)
    projectManager.save()
    return HttpResponse (f"""
    <p> Jefe de proyecto:{projectManager.nombre} {projectManager.apellido} ha sido creado </p>""")

def tarea(req,nombreTarea,fechaInicio,fechaTermino,estado):
    tarea=Tareas(nombreTarea=nombreTarea,fechaInicio=fechaInicio,fechaTermino=fechaTermino,estado=estado)
    tarea.save()
    return HttpResponse (f"""
    <p> Tarea:{tarea.nombreTarea} ha sido creada)""")






