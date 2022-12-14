"""primer_proyecto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from primer_proyecto.views import *
import primer_proyecto.settings as settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("saludo/",saludo),
    path("login/",iniciar_sesion),
    path("fecha/<nombre>/",dia_hoy),
    path("edad/<edad>/",anio_nacido),
    path("plantilla/",vista_plantilla),
    path("listado/",vista_listado_alumnos),
    path("aplicacion1/", include("aplicacion1.urls")),
    
]

#agregar las url de archivos estáticos
urlpatterns += static(prefix=settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)