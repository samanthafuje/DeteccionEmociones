from django.urls import path
from .views import registrar_alumno
from .views import estilos_aprendizaje
from . import views

urlpatterns = [
    path('registrar_alumno/', views.registrar_alumno, name='registrar_alumno'),
    
    path('estilos_aprendizaje/', views.estilos_aprendizaje, name='estilos_aprendizaje'),
]