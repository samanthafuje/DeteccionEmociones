from django.urls import path
from .views import registrar_alumno

urlpatterns = [
    path('registrar_alumno/', registrar_alumno, name='registrar_alumno'),
]