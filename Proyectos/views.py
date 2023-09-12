from django.shortcuts import render
from django.http import HttpResponse
from .models import Proyecto
from .models import ProjectManager
from .models import Tareas
from Proyectos.forms import ProyectoFormulario
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
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

def inicio(request):
    return render(request,"Proyectos/inicio.html")

def proyectos(request):
    return render(request,"Proyectos/proyectos.html")

def projectManagers(request):
    return render(request,"Proyectos/projectmanagers.html")

def tareas(request):
    return render(request,"Proyectos/tareas.html")
#formularios
#def proyectoFormulario(request):
#   return render(request,"Proyectos/formulario_proyecto.html")

# def pmsFormulario(request):
#     return render(request,"Proyectos/formulario_pm.html")

# def tareaFormulario(request):
#     return render(request,"Proyectos/formulario_tarea.html")
  
def proyectoFormulario(request):
 
      if request.method == "POST":
 
            miFormulario = ProyectoCreate(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)
 
            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  proyecto = Proyecto(nombre=informacion["nombre"], codigo=informacion["codigo"])
                  proyecto.save()
                  return render(request, "Proyectos/inicio.html")
      else:
            miFormulario = proyectoFormulario()
 
      return render(request, "Proyectos/formulario_proyecto.html", {"miFormulario": miFormulario})


class ProyectoCreate(CreateView):
    model = Proyecto
    template_name = "Proyectos/formulario_proyecto.html"
    fields = ['nombre', 'codigo']
    success_url = '/AppProyectos/'







