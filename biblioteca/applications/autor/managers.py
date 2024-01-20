from django.db import models
from django.db.models import Q 


class AutorManager(models.Manager):
    #este es el manager para el modelo autor 

    def listarAutores(self):
        return self.all()
    
    def buscarAutor(self, kword):
        resultado = self.filter(
            nombre__icontains = kword
        )
        return resultado
    
    def buscarAutorApellido(self, kword):
        resultado = self.filter(
            Q(nombre__icontains = kword) | Q(apellidos__icontains = kword)
        )
        return resultado
    
    def buscarAutorEdad(self, kword):
        resultado = self.filter(
            nombre__icontains = kword
        ).exclude(edad = 100)
        return resultado
    

    def autoEdadMayorMenor (self, kwor):
        resultado = self.filter(
            edad__gt = 40,
            edad__lt = 100
        ).order_by('apellidos', 'nombre', 'id')
        return resultado
