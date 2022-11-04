from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context, loader



def saludo(request):
    return HttpResponse("""
    <h1>Hola coders! :) </h1>
    <p style='color:red' >Esto es una prueba</p>
    """)


def iniciar_sesion(request):
    return HttpResponse("pasame tu usuario")

def dia_hoy(request,nombre):
    hoy = datetime.now()

    respuesta = f"Hoy es {hoy} - Bienvenido {nombre}"
    return HttpResponse(respuesta)

def anio_nacido(request,edad):
    hoy = datetime.now().year
    edad = int(edad)
    
    nacido = f"Estamos en el año {hoy} y vos naciste en el año {hoy-edad}"
    return HttpResponse(nacido)

def vista_plantilla(request):
    archivo = open(r"E:\Gonzalo\Python\17-Django\primer_proyecto\primer_proyecto\templates\plantilla.html")
    plantilla = Template(archivo.read())

    archivo.close

    #creo un diccionario con claves y contenido que luego pasaré como contexto
    datos = {"nombre": "Gonzalo","apellido":"Garcia","fecha":datetime.now(),"edad":48,"altura":1.85} 

    #acá le paso el diccionario como contexto
    contexto = Context(datos)

    documento = plantilla.render(contexto)
    return HttpResponse(documento)


def vista_listado_alumnos(request):

    archivo = open(r"E:\Gonzalo\Python\17-Django\primer_proyecto\primer_proyecto\templates\vista_listado_alumnos.html")

    plantilla = Template(archivo.read())

    archivo.close()

    listado_alumnos = ["Gonzalo Garcia","Diego Galdeano", "Santiago Falconi","Juliana Garcia"]
        
    #creamos el diccionario de contexto
    datos = {"tecnologia":"Python","listado_alumnos": listado_alumnos}

    #creamos el contexto
    contexto = Context(datos)


    documento = plantilla.render(contexto)
    return HttpResponse(documento)


def vista_listado_alumnos_2(request):
    plantilla = loader.get_template("vista_listado_alumnos.html")
    
    lista_alumnos = ["Gonzalo Garcia","Diego Galdeano", "Santiago Falconi","Juliana Garcia"]
        
    #creamos el diccionario de contexto
    datos = {"tecnologia":"Python","listado":lista_alumnos}

    documento = plantilla.render(datos)

    return HttpResponse(documento)
    