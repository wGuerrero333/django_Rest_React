from rest_framework import serializers
# como proveer los datos del MODELO para poder serializar ?
# se importa la calse Tarea del archivo models dado que esos campos on los que se vana aserializar
from .models import task

#la serializacion convierte le tipo de dato que entrega django convirte PYTHON en json

class Taskserializer(serializers.ModelSerializer):
    class Meta:
        model = task
        # fields = ['id','title','objetivo','done']
        fields = '__all__'