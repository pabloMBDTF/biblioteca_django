from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render

# Create your views here.

from django.views.generic import ListView


from .models import Autor


class ListAutores(ListView):
    #model = Autor
    context_object_name = 'listaAutores'
    template_name = 'autor/lista.html'

    def get_queryset(self):
        palabraClave = self.request.GET.get("kword", "")
        return Autor.objects.autoEdadMayorMenor(palabraClave) 