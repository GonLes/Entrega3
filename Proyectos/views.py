from django.shortcuts import render
from django.http import HttpResponse
from .models import Proyecto
from .models import ProjectManager
from .models import Tareas
from Proyectos.forms import ProyectoFormulario , TareaFormulario
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

def buscarProyectos(request):
     return render(request,'Proyectos/buscar_proyecto.html')

#def buscar(request):
     
#formularios
#def proyectoFormulario(request):
#   return render(request,"Proyectos/formulario_proyecto.html")

# def pmsFormulario(request):
#     return render(request,"Proyectos/formulario_pm.html")

# def tareaFormulario(request):
#     return render(request,"Proyectos/formulario_tarea.html")
####################FORMULARIO PROYECTO###########################  
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


##################FORMULARIO TAREA####################################
class TareaCreate(CreateView):
    model = Tareas
    template_name = "Proyectos/formulario_tarea.html"
    fields = ['nombreTarea', 'fechaInicio', 'fechaTermino','estado']
    success_url = '/AppProyectos/'

def tareaFormulario(request):
 
      if request.method == "POST":
 
            miFormulario = TareaCreate(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)
 
            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  tarea = Tareas(nombreTarea=informacion["nombreTarea"], fechaInicio=informacion["fechaInicio"], fechaTermino=informacion["fechaTermino"])
                  tarea.save()
                  return render(request, "Proyectos/inicio.html")
      else:
            miFormulario = proyectoFormulario()
 
      return render(request, "Proyectos/formulario_tarea.html", {"miFormulario": miFormulario})
##################FORMULARIO PMs####################################
class projectManagerCreate(CreateView):
    model = ProjectManager
    template_name = "Proyectos/formulario_Pm.html"
    fields = ['nombre', 'apellido', 'email']
    success_url = '/AppProyectos/'

def pmFormulario(request):
 
      if request.method == "POST":
 
            miFormulario = projectManagerCreate(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)
 
            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  project_manager = ProjectManager(nombre=informacion["nombre"], apellido=informacion["apellido"], email=informacion["email"])
                  project_manager.save()
                  return render(request, "Proyectos/inicio.html")
      else:
            miFormulario = pmFormulario()
 
      return render(request, "Proyectos/formulario_Pm", {"miFormulario": miFormulario})





