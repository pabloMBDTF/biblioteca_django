from datetime import date
from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.http import HttpResponseRedirect 
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

        # con este metodo lo que se hace es crear un nuevo registro en la base de datos
        # Prestamo.objects.create(
        #     lector = form.cleaned_data['lector'],
        #     libro = form.cleaned_data['libro'],
        #     fechaPrestamo = date.today(),
        #     devuelto = False

        # )

        # con este metodo lo que se hace es actualizar un registr existente o en caso de que no exista,
        # crear uno nuevo 
        libro = form.cleaned_data['libro']
        if (libro.stok >= 1):
            prestamo = Prestamo(
                lector = form.cleaned_data['lector'],
                libro = form.cleaned_data['libro'],
                fechaPrestamo = date.today(),
                devuelto = False
            )
            #libro = form.cleaned_data['libro']
            libro.stok = libro.stok - 1

            prestamo.save()
            libro.save()
        else:
            print("no hay disponibilidad.")
        return super(RegistrarPrestamo, self).form_valid(form)
    


class AddPrestamo(FormView):
    template_name = 'lector/prestamos/agregar.html'
    form_class = PrestamoForm
    success_url = '.'

    def form_valid(self, form):
        obj, crated = Prestamo.objects.get_or_create(
            lector = form.cleaned_data['lector'],
            libro = form.cleaned_data['libro'],
            devuelto = False,
            defaults = {
                'fechaPrestamo': date.today()
            }
        )
        if crated:
            return super(AddPrestamo, self).form_valid(form)
        else:
            return HttpResponseRedirect('/')

       
        