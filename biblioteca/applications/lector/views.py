from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render

# Create your views here.

from django.views.generic import ListView


from .models import Lector

class listarLectores(ListView):
    #model = Autor
    context_object_name = 'listaLector'
    template_name = 'lector/lista.html'

    def get_queryset(self):
        return Lector.objects.listarLectores() 