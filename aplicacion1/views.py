from django.shortcuts import render
from django.http import HttpResponse

def estudiantes(request):
    return HttpResponse("Estas en estudiantes")

def profesores(request):
    return HttpResponse("Estas en profesores")

def cursos(request):
    return HttpResponse("Estas en cursos")

def inicio(request):
    return render(request, "aplicacion1/inicio.html")


