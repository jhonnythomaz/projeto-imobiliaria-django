# imoveis/admin.py

from django.contrib import admin
from .models import Imovel, FotoImovel

# Esta classe permite adicionar fotos diretamente na tela de edição do imóvel (inline)
class FotoImovelInline(admin.TabularInline):
    model = FotoImovel
    extra = 1 # Quantos campos de upload de foto extra devem aparecer

class ImovelAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'localizacao', 'preco', 'corretor_responsavel', 'disponivel')
    list_filter = ('disponivel', 'tipo_imovel')
    search_fields = ('titulo', 'localizacao', 'descricao')
    inlines = [FotoImovelInline]

admin.site.register(Imovel, ImovelAdmin)