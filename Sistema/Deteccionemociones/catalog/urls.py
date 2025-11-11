from django.urls import path
from .views import registrar_alumno
from . import views

urlpatterns = [
    path('registrar_alumno/', views.registrar_alumno, name='registrar_alumno'),
]