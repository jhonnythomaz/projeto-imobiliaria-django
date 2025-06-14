# imoveis/urls.py - CÓDIGO FINAL COM TODAS AS ROTAS

from django.urls import path
from . import views

app_name = 'imoveis'

urlpatterns = [
    # Rota 1: Lista de imóveis
    path('', views.lista_imoveis, name='lista_imoveis'),
    
    # Rota 2: Detalhes de um imóvel
    path('<uuid:imovel_id>/', views.detalhe_imovel, name='detalhe_imovel'),
    
    # Rota 3: Adicionar um novo imóvel
    path('adicionar/', views.criar_imovel, name='criar_imovel'),
    
    # --- ROTA 4: A NOVA ROTA DE EDIÇÃO ---
    # Captura o ID do imóvel e o 'editar/' no final da URL
    path('<uuid:imovel_id>/editar/', views.editar_imovel, name='editar_imovel'),
]