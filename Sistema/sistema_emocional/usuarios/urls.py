
from django.urls import path

from .views import (
    registro,
    login_view,
    inicio,
    test_estilos,
    logout_view,
    dass21,
    test_dass21,
    resultado_dass21,
    captura_texto,
    mis_reportes,
    detalle_reporte,
)


urlpatterns = [

    path('registro/', registro, name='registro'),

    path('login/', login_view, name='login'),

    path('inicio/', inicio, name='inicio'),

    path('test-estilos/', test_estilos, name='test_estilos'),

    path('dass21/', dass21, name='dass21'),

    path('test-dass21/', test_dass21, name='test_dass21'),

    path(
        'resultado-dass21/<int:evaluacion_id>/',
        resultado_dass21,
        name='resultado_dass21'
    ),

    path('logout/', logout_view, name='logout'),

    path('captura-texto/', captura_texto, name='captura_texto'),

    # REPORTES INDIVIDUALES
    path(
        'mis-reportes/',
        mis_reportes,
        name='mis_reportes'
    ),

    path(
        'mis-reportes/<int:texto_id>/',
        detalle_reporte,
        name='detalle_reporte'
    ),

]
