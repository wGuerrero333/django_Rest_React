from django.db import models

# Este MODELO de tareas permite guardar datos desde le panel de admnistrador de django
# django tiene su propio ORM
# Charfield inica que sera un campo CHAR en la db
# si no le pasan nada a description (campo de tiempo)que marque como vacio  blank=Truepara que
# si se agregan campos a la tabla para que los reconozca se debe:
# python manage.py makemigrations <name table>
# python manage.py migrate <name table>
#  es INDISPENSABLE poner algo por default  para que la tabla llene el campo dado que NO acepta campos vacios

class task (models.Model):
    title = models.CharField(max_length=200)
    time = models.TimeField(blank=True)
    objetivo = models.CharField(max_length=200, default=True)

    done = models.BooleanField(default=False)
# con el metodo self permite acceder ver el title de cada instancia  (tabla)
    def __str__(self):
        return self.title

