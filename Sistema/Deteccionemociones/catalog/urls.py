from django.urls import path
from . import views

urlpatterns = [
    path('registrar_alumno/', views.registrar_alumno, name='registrar_alumno'),
    path('estilos_aprendizaje/<int:id_alumno>/', views.estilos_aprendizaje, name='estilos_aprendizaje'),
]