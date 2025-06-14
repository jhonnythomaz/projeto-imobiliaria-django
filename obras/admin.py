# obras/admin.py

from django.contrib import admin
from .models import Obra, StatusObra

class StatusObraInline(admin.TabularInline):
    model = StatusObra
    extra = 1

class ObraAdmin(admin.ModelAdmin):
    list_display = ('imovel', 'data_inicio', 'previsao_entrega', 'status_atual')
    inlines = [StatusObraInline]

admin.site.register(Obra, ObraAdmin)