# imoveis/forms.py - CÓDIGO FINAL COM AMBOS OS FORMULÁRIOS

from django import forms
from .models import Imovel, FotoImovel # 1. Importamos o model FotoImovel também

# --- Formulário para os dados principais do Imóvel ---
class ImovelForm(forms.ModelForm):
    # A classe 'Meta' diz ao Django de qual model criar o formulário
    # e quais campos incluir.
    class Meta:
        model = Imovel
        
        # Listamos aqui os campos do nosso Model 'Imovel' que queremos
        # que o corretor preencha.
        fields = [
            'titulo', 
            'descricao', 
            'localizacao', 
            'preco', 
            'numero_quartos', 
            'tipo_imovel'
        ]

# --- Formulário para o upload de Fotos do Imóvel ---
class FotoImovelForm(forms.ModelForm):
    # Este formulário é específico para o upload de uma única foto.
    class Meta:
        model = FotoImovel
        
        # O único campo que o usuário irá preencher neste formulário é o da imagem.
        # O campo 'imovel' será associado automaticamente na nossa view.
        fields = ['imagem']
        
        # Podemos adicionar 'labels' para deixar os nomes dos campos mais amigáveis.
        labels = {
            'imagem': 'Selecione uma imagem',
        }