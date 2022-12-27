from django.urls import path
from .views import *
from django.contrib.auth. views import LogoutView


urlpatterns = [
    path('inicio/', inicio, name='inicio'),

    path('posteos/', posteos, name='posteos'),
    path('nuevoPost/', postFormulario, name='nuevoPost'),
    path('lista_posteos/', lista_posteos, name='lista_posteos'),


]