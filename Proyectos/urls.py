from django.urls import path
from Proyectos import views
from .views import *

urlpatterns = [
    path('', inicio, name= "Inicio"),
    path('Proyectos/', proyectos, name="Proyectos"),
    path('ProjectManagers/', projectManagers, name="ProjectManagers"),
    path('Tareas/', tareas, name="Tareas"),
    path('busquedaProyecto/', busquedaProyectos, name="busquedaProyecto"),
    path('buscar/',buscar,name="buscar"),
    path('AgregaProyecto/', ProyectoCreate.as_view(), name="AgregaProyecto"),
    path('AgregaPm/', projectManagerCreate.as_view(), name="AgregaPm"),
    path('AgregaTarea/', TareaCreate.as_view(), name="AgregaTarea"),
        
]