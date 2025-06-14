# imoveis/models.py

from django.db import models
from django.conf import settings # Importa as configurações do projeto para pegar o AUTH_USER_MODEL
import uuid

# --- Model Imovel ---
# Representa um imóvel no sistema.
class Imovel(models.Model):

    # Opções para o campo 'tipo_imovel'
    TIPO_IMOVEL_CHOICES = [
        ('CASA', 'Casa'),
        ('APARTAMENTO', 'Apartamento'),
        ('TERRENO', 'Terreno'),
    ]

    # Campos da tabela
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    titulo = models.CharField(max_length=100, verbose_name="Título do Anúncio")
    descricao = models.TextField(blank=True)
    localizacao = models.CharField(max_length=255)
    preco = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="Preço")
    numero_quartos = models.PositiveIntegerField(verbose_name="Nº de Quartos")
    disponivel = models.BooleanField(default=True, verbose_name="Disponível para Venda")
    
    tipo_imovel = models.CharField(max_length=20, choices=TIPO_IMOVEL_CHOICES, verbose_name="Tipo de Imóvel")
    
    # --- Relacionamentos (Foreign Key) ---
    
    # Qual corretor é responsável por este imóvel?
    # Usamos settings.AUTH_USER_MODEL para referenciar nosso model Usuario customizado.
    # on_delete=models.SET_NULL: Se o corretor for deletado, o campo no imóvel fica nulo, mas o imóvel não é apagado.
    # limit_choices_to: No painel admin, só vai mostrar usuários que são 'CORRETOR' para selecionar.
    corretor_responsavel = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        limit_choices_to={'tipo_usuario': 'CORRETOR'},
        verbose_name="Corretor Responsável"
    )
    
    data_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.titulo} - {self.localizacao}"

# --- Model FotoImovel ---
# Permite que cada imóvel tenha um número ilimitado de fotos.
class FotoImovel(models.Model):

    # Relacionamento: Esta foto pertence a qual imóvel?
    # on_delete=models.CASCADE: Se o imóvel for deletado, todas as suas fotos também serão.
    # related_name='fotos': Permite que a gente acesse as fotos de um imóvel usando 'imovel.fotos.all()'.
    imovel = models.ForeignKey(Imovel, related_name='fotos', on_delete=models.CASCADE)
    
    # O Django vai precisar de uma biblioteca para lidar com imagens (Pillow).
    # upload_to='fotos_imoveis/': As imagens serão salvas numa pasta chamada 'fotos_imoveis' dentro da sua pasta de media.
    imagem = models.ImageField(upload_to='fotos_imoveis/', verbose_name="Foto")

    def __str__(self):
        return f"Foto de {self.imovel.titulo}"