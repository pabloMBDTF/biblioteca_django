from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('libros/', views.listarLibros.as_view(), name = "libros"),
    path('librosCategoria/', views.listarLibros2.as_view(), name = "librosCategoria"),
    path('librosDetalle/<pk>/', views.LibroDetalle.as_view(), name = "librosDetalle"),
]