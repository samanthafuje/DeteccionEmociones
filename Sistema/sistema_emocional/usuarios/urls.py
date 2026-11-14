
from django.urls import path

from .views import (
    registro,
    login_view,
    inicio,
    test_estilos,
    logout_view,
    dass21
)


urlpatterns = [

    path(
        'registro/',
        registro,
        name='registro'
    ),

    path(
        'login/',
        login_view,
        name='login'
    ),

    path(
        'inicio/',
        inicio,
        name='inicio'
    ),

    path(
        'test-estilos/',
        test_estilos,
        name='test_estilos'
    ),

    path(
        'dass21/',
        dass21,
        name='dass21'
    ),

    path(
        'logout/',
        logout_view,
        name='logout'
    ),

]
