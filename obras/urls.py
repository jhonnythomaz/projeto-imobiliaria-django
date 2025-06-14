# obras/urls.py - CÓDIGO CORRETO

from django.urls import path
from . import views

app_name = 'obras'

urlpatterns = [
    # Aponte para a view correta: 'views.lista_obras'
    path('', views.lista_obras, name='lista_obras'),
]