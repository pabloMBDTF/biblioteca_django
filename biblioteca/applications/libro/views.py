from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView
from .manegers import *


from .models import Libro

class listarLibros(ListView):
    #model = Autor
    context_object_name = 'listaLibro'
    template_name = 'libro/lista.html'

    def get_queryset(self):
        palabraClave = self.request.GET.get("kword", '')
        fecha1 = self.request.GET.get("fecha1", '')
        fecha2 = self.request.GET.get("fecha2", '')
        print(fecha1)
        print(fecha2)

        if (fecha1 and fecha2):
            return Libro.objects.retornarLibrosPorFecha(palabraClave, fecha1, fecha2)
        else:
            return Libro.objects.listarLibroNombre(palabraClave)


class listarLibros2(ListView):
    context_object_name = 'listaLibros'
    template_name = 'libro/listaCategoria.html'
    palabraClave = '1'

    def get_queryset(self):
        return Libro.objects.listarPorCategoria(self.palabraClave)
    

class LibroDetalle(DetailView):
    model = Libro
    template_name = "libro/libroDetalle.html"


        
    