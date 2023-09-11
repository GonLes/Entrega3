from django.urls import path
from Proyectos import views
from .views import *

urlpatterns = [
    path('', inicio),
    path('proyectos/', proyectos),
    path('projectManagers/', projectManagers),
    path('tareas/', tareas),
]