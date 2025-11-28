from django.db import models

# Create your models here.
class Actividad(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha = models.DateField()

    def __str__(self):
        return self.titulo