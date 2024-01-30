from django.db import models

# Create your models here.

class Persona(models.Model):
    """Model definition for Persona."""
    fullName = models.CharField('nombres', max_length = 50)
    pais = models.CharField('Pais', max_length = 50)
    pasaporte = models.CharField('Pasaporte', max_length = 60 )
    apodo = models.CharField('apodo', max_length = 20)


    

    class Meta:
        """Meta definition for Persona."""

        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'
        db_table = 'Persona'
        unique_together = ['pais', 'apodo']

    def __str__(self):
        return self.id + ' ' + self.fullName + ' ' + self.pasaporte
        
