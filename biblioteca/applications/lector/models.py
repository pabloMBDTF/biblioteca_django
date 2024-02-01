from django.db import models
from applications.autor.models import Persona

from applications.libro.models import Libro
from .managers import LectorManager, PrestamoManager
 

# Create your models here.


class Lector (Persona):
    

    objects = LectorManager()

    
    

    
class Prestamo (models.Model):
    lector = models.ForeignKey(
        Lector,
        on_delete = models.CASCADE,
        related_name = 'libroPrestamo'

    )

    libro = models.ForeignKey(
        Libro,
        on_delete = models.CASCADE,
        # entonces recuerda que este related name unicamente lo podras usar en las funciones del manager de Libro
        related_name = 'libroPrestamo'
    )

    fechaPrestamo = models.DateField()

    fechaDevolucion = models.DateField(
        blank = True, 
        null = True
    )

    devuelto = models.BooleanField()

    objects = PrestamoManager()

    def __str__ (self):
        return self.lector.nombre + ' - ' + self.libro.titulo
