from django.db import models

# Create your models here.

# Managers
from .managers import AutorManager


class Persona(models.Model):
    nombre = models.CharField(
        max_length = 50
    )
    apellidos = models.CharField(
        max_length = 60
    )
    nacionalidad = models.CharField(
        max_length = 35
    )
    edad = models.PositiveBigIntegerField(
        default = 0
    )

    def __str__ (self):
        return str(self.id) + ' - ' + self.nombre + " " + self.apellidos
    
    class Meta:
        abstract = True


class Autor(Persona):
    
    objects = AutorManager()

    
