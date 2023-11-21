from django.urls import path, include
from rest_framework import routers
from apps import views
# se crean las rutas
router = routers.DefaultRouter()
router.register(r'tasks', views.TaskView)
#Genera get put ...
# recibe 2 parametros: 
# 1. nombre de la URL (como va a ser visitada la URL),
# 2.Que es lo que se va a ejecutar osea url generada por django (routers) 

urlpatterns = [
    path("api/v1/", include(router.urls) )
]

