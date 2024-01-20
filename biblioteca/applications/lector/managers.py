from django.db import models


class LectorManager(models.Manager):
    #este es el manager para el modelo autor 

    def listarLectores(self):
        return self.all()