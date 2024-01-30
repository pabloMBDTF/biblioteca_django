from django.db import models
from applications.autor.models import Autor

from .manegers import LibroManager, CategoriaManager
# Create your models here.


class Categoria (models.Model):
    nombre = models.CharField(
        max_length = 80
    )

    objects = CategoriaManager()

    def __str__ (self):
        return 'categoria: ' + self.nombre + ' - ' + str(self.id)
    

class Libro (models.Model):
    titulo = models.CharField(
        max_length = 80
    )

    # esta es una llave foranea unica es decir este objeto contiene solo una categoria 
    categoria = models.ForeignKey(
        Categoria, on_delete = models.CASCADE,
        related_name = 'categoriaLibro'
    )

    # en este caso son varias llaves foraneas, es decir este objeto tendra varias llaves de tipo autor, varios autores 
    autores = models.ManyToManyField(
        Autor
    )

    fechaLanzamiento = models.DateField(
        'fecha de lanzamiento'
    )

    portada = models.ImageField(
        upload_to='portal'
    )

    visitas = models.PositiveIntegerField(

    )

    objects = LibroManager()

    class Meta:
        # como quiero que aparesca el numbre en pluaral
        verbose_name_plural = 'Libros'
        # por que parametros quiero que se ordene en el administrador
        ordering = ['titulo', 'fechaLanzamiento']

    def __str__(self):
        return str(self.id) + ' - ' + self.titulo



