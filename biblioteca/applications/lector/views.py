from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from .models import Prestamo


# Create your views here.

from django.views.generic import ListView, FormView
from .forms import PrestamoForm


from .models import Lector

class listarLectores(ListView):
    #model = Autor
    context_object_name = 'listaLector'
    template_name = 'lector/lista.html'

    def get_queryset(self):
        return Lector.objects.listarLectores() 
    

class RegistrarPrestamo(FormView):
    template_name = 'lector/prestamos/agregar.html'
    form_class = PrestamoForm
    success_url = '.'

    def form_valid(self, form):
        return super(RegistrarPrestamo, self).form_valid(form)