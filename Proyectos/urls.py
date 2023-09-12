from django.urls import path
from Proyectos import views
from .views import *

urlpatterns = [
    path('', inicio, name= "Inicio"),
    path('Proyectos/', proyectos, name="Proyectos"),
    path('ProjectManagers/', projectManagers, name="ProjectManagers"),
    path('Tareas/', tareas, name="Tareas"),
    path('AgregaProyecto/', ProyectoCreate.as_view(), name="AgregaProyecto"),
    #path('AgregaPm', pmsFormulario, name="AgregaPm"),
    #path('AgregaTarea', tareaFormulario, name="AgregaTarea"),
]