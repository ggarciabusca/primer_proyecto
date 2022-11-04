from django.urls import path
from aplicacion1.views import *

urlpatterns = [
    path("",inicio),
    path("estudiantes/", estudiantes),
    path("profesores/", profesores),
    path("cursos/", cursos)
]