from itertools import count
from django.db import models
from django.db.models import Q, Count, Avg


class LectorManager(models.Manager):
    #este es el manager para el modelo autor 

    def listarLectores(self):
        return self.all()
    

    def numLectoresPrestamos(self):
        resultado = self.aggregate (
            numPrestamo = count(
                'libroPrestamo'
            )
        )
        return resultado
    
class PrestamoManager(models.Manager):

    # en esta funcion estamos calculando el promedio de edad de los lectores que an solicitado un numero en especifico 

    def edadPromedioPrestamos(self):
        resultado = self.filter(libro__id = '4').aggregate(promedioEdad = Avg('lector__edad'))
        return resultado
        
    #funcion para saber cuantas veces se a prestado un libro 

    def numLibrosPrestado(self):
        resultado = self.annotate(
            numPrestado = Count('libro')
        ) 

        for r in resultado:
            print("===============")
            print(r, r.numPrestado)
        return resultado
            