# imoveis/models.py - VOLTANDO PARA A SOLUÇÃO SIMPLES E EFICAZ

from django.db import models
from django.conf import settings
import uuid

class Imovel(models.Model):
    TIPO_IMOVEL_CHOICES = [
        ('CASA', 'Casa'),
        ('APARTAMENTO', 'Apartamento'),
        ('TERRENO', 'Terreno'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    titulo = models.CharField(max_length=100, verbose_name="Título do Anúncio")
    descricao = models.TextField(blank=True)
    localizacao = models.CharField(max_length=255)
    preco = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="Preço")
    
    # --- AQUI ESTÁ A ÚNICA MUDANÇA REAL ---
    # Tornamos o campo opcional, com um valor padrão de 0.
    numero_quartos = models.PositiveIntegerField(verbose_name="Nº de Quartos", default=0)
    
    disponivel = models.BooleanField(default=True, verbose_name="Disponível para Venda")
    tipo_imovel = models.CharField(max_length=20, choices=TIPO_IMOVEL_CHOICES, verbose_name="Tipo de Imóvel")
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

class FotoImovel(models.Model):
    imovel = models.ForeignKey(Imovel, related_name='fotos', on_delete=models.CASCADE)
    imagem = models.ImageField(upload_to='fotos_imoveis/', verbose_name="Foto")

    def __str__(self):
        return f"Foto de {self.imovel.titulo}"