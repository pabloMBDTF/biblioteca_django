from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('lectores/', views.listarLectores.as_view(), name = "lectores"),
    path('crear-prestamo/', views.RegistrarPrestamo.as_view(), name = "crear_prestamo"),
]