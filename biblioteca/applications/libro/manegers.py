from django.db import models
from django.db.models import Q, Count

class LibroManager(models.Manager):
    #este es el manager para el modelo autor 

    def listarLibros(self):
        return self.all()
    
    def listarLibroNombre(self, kword):
        resultado = self.filter(titulo__icontains = kword)
        return resultado 
    
    def retornarLibrosPorFecha(self, kword, fecha1, fecha2):
        resultado = self.filter(
            titulo__icontains = kword,
            fechaLanzamiento__range = (fecha1, fecha2)
        )
        return resultado
    
    def listarPorCategoria(self, categoria):
        
        return self.filter(categoria__id = categoria).order_by('titulo')
    
    def addAutorLibro (self, libroId, autor):
        libro = self.get(id = libroId)
        libro.autores.add(autor)
        return libro
    

class CategoriaManager (models.Manager):

    def categoriaAutores(self, autor):
        return self.filter(
            categoriaLibro__autores__id = autor
        ).distinct()
    

    # con esta funcion me retorna la cantidad de libros que hay por categoria 
    def listarCategoria (self):
        resultado = self.annotate(
            numLibros = Count('categoriaLibro')
        )
        return resultado


    
    