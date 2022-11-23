from django.shortcuts import render,redirect
from aplicacion1.models import *
from django.http import HttpResponse
from aplicacion1.forms import ProfesorFormulario, UserRegisterForm

#para el login importo el formulario
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm

#importo las funciones de login
from django.contrib.auth import login,logout,authenticate



def estudiantes(request):
    return render(request,"aplicacion1/estudiantes.html")

def profesores(request):
    return render(request,"aplicacion1/profesores.html")

def creacion_profesores(request):
    if request.method == "POST":
        formulario = ProfesorFormulario(request.POST)
        if formulario.is_valid():
            #recuperamos los datos del atributo cleaned_data
            data = formulario.cleaned_data
            profesor = Profesor(nombre=data["nombre"], apellido=data["apellido"], email=data["email"],profesion=data["profesion"])
            profesor.save()

    
    formulario = ProfesorFormulario()
    contexto = {"formulario": formulario}
    return render(request,"aplicacion1/profesores_formulario.html",contexto)

def cursos(request):
    cursos = Curso.objects.all()
    contexto = {"listado_cursos":cursos}

    return render(request,"aplicacion1/cursos.html",contexto)

def inicio(request):
    return render(request, "aplicacion1/inicio.html")

#voy a crear una vista para introducir info en mi base de datos desde un formulario
def creacion_curso(request):
    if request.method == "POST":
        nombre_curso = request.POST["curso"]
        numero_camada = int(request.POST["camada"])

        curso = Curso(nombre=nombre_curso, camada=numero_camada)
        curso.save()

    return render(request,"aplicacion1/curso_formulario.html")


def ingreso(request):
    
    if request.method =="POST":
        formulario = AuthenticationForm(request,data=request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            user = authenticate(username=data["username"], password=data["password"])
            #la funcion authenticate me va a devolver un usuario o none

            if user is not None:
                login(request,user)
                return redirect("inicio")
            
            else:
                return render(request,"aplicacion1/login.html",{"form":formulario,"errors":"Credenciales Invalidas"})

        else:
                return render(request,"aplicacion1/login.html",{"form":formulario,"errors":errors})



    formulario = AuthenticationForm()
    return render(request, "aplicacion1/login.html",{"form":formulario})

def registrar_usuario(request):
    
    if request.method == "POST":
        formulario = UserRegisterForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect("inicio")
        else:
            return render(request, "aplicacion1/registrar_usuario.html",{"form":formulario,"errors":formulario.errors})

    formulario = UserRegisterForm()
    return render(request, "aplicacion1/registrar_usuario.html",{"form":formulario})