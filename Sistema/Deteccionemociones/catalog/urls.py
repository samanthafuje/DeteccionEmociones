from django.urls import path
from . import views

urlpatterns = [
    path('registrar_alumno/', views.registrar_alumno, name='registrar_alumno'),
    path('estilos_aprendizaje/<int:alumno_id>/', views.estilos_aprendizaje_view, name='estilos_aprendizaje'),
    path('resultado/<int:alumno_id>/', views.resultado_estilo, name='resultado_estilo'),
]