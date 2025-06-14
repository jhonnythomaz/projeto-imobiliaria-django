# obras/models.py

from django.db import models
from imoveis.models import Imovel  # Precisamos saber a qual imóvel a obra pertence
import uuid

# --- Model Obra ---
# Cada imóvel que está em construção terá um registro de Obra associado.
class Obra(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    # --- Relacionamento (One-to-One) ---
    # OneToOneField garante que cada Imóvel só pode ter UMA Obra associada. É uma relação 1 para 1.
    # on_delete=models.CASCADE: Se o imóvel for deletado, sua obra também será.
    imovel = models.OneToOneField(Imovel, on_delete=models.CASCADE, verbose_name="Imóvel Associado")

    data_inicio = models.DateField(verbose_name="Data de Início")
    previsao_entrega = models.DateField(verbose_name="Previsão de Entrega")
    
    # Campo para um resumo do status atual, para fácil visualização
    status_atual = models.CharField(max_length=100, blank=True, verbose_name="Status Atual")

    def __str__(self):
        return f"Obra do Imóvel: {self.imovel.titulo}"

# --- Model StatusObra ---
# Registra cada atualização no andamento da obra, criando um histórico.
class StatusObra(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    # --- Relacionamento (Foreign Key) ---
    # related_name='historico_status': Permite acessar todos os status de uma obra com 'obra.historico_status.all()'.
    obra = models.ForeignKey(Obra, related_name='historico_status', on_delete=models.CASCADE, verbose_name="Obra")

    fase = models.CharField(max_length=50, verbose_name="Fase da Obra") # Ex: "Fundação", "Estrutura", "Acabamento"
    descricao = models.TextField(blank=True, verbose_name="Descrição da Atualização")
    percentual_concluido = models.PositiveIntegerField(verbose_name="Percentual Concluído (%)")
    data_atualizacao = models.DateTimeField(auto_now_add=True, verbose_name="Data da Atualização")

    class Meta:
        # 'ordering' define a ordem padrão ao buscar os registros.
        # O hífen '-' significa ordem decrescente (do mais novo para o mais antigo).
        ordering = ['-data_atualizacao']
        verbose_name = "Status da Obra"
        verbose_name_plural = "Status das Obras"

    def __str__(self):
        return f"{self.obra.imovel.titulo} - {self.fase} ({self.percentual_concluido}%)"