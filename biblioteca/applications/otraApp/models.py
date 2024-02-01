from django.db import models

# Create your models here.


class OtraPersona(models.Model):
    """Model definition for Persona."""

    nombre = models.CharField('nombre', max_length = 50)
    apellido = models.CharField('apellido', max_length = 50)
    pasaporte = models.CharField('pasaporte', max_length = 50)
    pais = models.CharField('Pais', max_length = 50)
    edad = models.PositiveBigIntegerField()
    apodo = models.CharField('apodo', max_length = 30)

    class Meta:
        """Meta definition for Persona."""

        verbose_name = 'OtraPersona'
        verbose_name_plural = 'OtraPersonas'
        unique_together = ['pais', 'apodo']
        constraints = [
            models.CheckConstraint(check = models.Q(edad__gte = 5), name = 'edadMayor')
        ]
        abstract = True

    def __str__(self):
        """Unicode representation of Persona."""
        return str(self.id)
    
    

class Trabajador (OtraPersona):
    puesto = models.CharField('puesto', max_length = 50)

    def __str__(self):
        return self.puesto