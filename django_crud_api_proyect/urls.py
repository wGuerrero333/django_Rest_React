"""
URL configuration for django_crud_api_proyect project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
# se añade las urls para que el proyecto las pueda usar
# DESDE el POSTMAN se pone http://localhost:8000 luego la ruta del urls.py  en el proyecto
#La anterior INCLUDE las ruta de urls.py de la app 
#Estas son las rutas principales de hay se desprenden las demas en urls.py de la APP
urlpatterns = [
    path('admin/', admin.site.urls),
    path('tasks/', include('apps.urls'))
]
