from rest_framework import viewsets
from .serializer import Taskserializer
from .models import task
# Create your views here.
# con una sola clase django genera todo el CRUD 
# con el serializar se le señala que campos convertir delcalse que ya se ha creado
# queryset= la lsita de elementos que estamos accediendo desde 
# el ORM (Atraves de clases manipular DB) de Django
class TaskView(viewsets.ModelViewSet):
    queryset = task.objects.all()

    serializer_class = Taskserializer