from django.urls import path, include
from rest_framework import routers
from rest_framework.documentation import include_docs_urls
from apps import views
# se crean las rutas de la app ejemplo: la ultima parte de esta ruta despues del puerto " r'tasks' "
#  http://127.0.0.1:8000/tasks/api/v1/tasks/
router = routers.DefaultRouter()
# La r en este end point sirve para que no escape cuando la ruta tenga un /
router.register(r'tasks', views.TaskView)
#Genera get put ...
# recibe 2 parametros: 
# 1. nombre de la URL (como va a ser visitada la URL),
# 2.Que es lo que se va a ejecutar osea url generada por django (router) 

urlpatterns = [
    path("api/v1/", include(router.urls) ),
    path("documentacion/", include_docs_urls(title="Documentacion de la API"))
]

