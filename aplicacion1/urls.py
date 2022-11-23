from django.urls import path
from aplicacion1.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("",inicio, name="inicio"),
    path("estudiantes/", estudiantes),
    path("profesores/", profesores),
    path("cursos/", cursos),
    path("cursos/crear/",creacion_curso,name="coder-cursos-crear"),
    path("profesores/crear/",creacion_curso,name="coder-profesores-crear"),
    path("login/", ingreso, name="login"),
    path("registro/", registrar_usuario, name="registro"),
    path("logout/",LogoutView.as_view(template_name="aplicacion1/logout.html"),name="logout")
]