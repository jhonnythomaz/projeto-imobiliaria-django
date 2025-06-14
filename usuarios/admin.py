# usuarios/admin.py - CÓDIGO CORRIGIDO E MELHORADO

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario

# Esta classe define como o nosso model Usuario será exibido e gerenciado
# no painel de administração.
class CustomUserAdmin(UserAdmin):
    # O model que este admin gerencia
    model = Usuario
    
    # --- Configuração da tela de LISTA de usuários ---
    # Campos que aparecem na lista de usuários
    list_display = ('email', 'username', 'tipo_usuario', 'is_staff', 'is_active')
    # Filtros que aparecem na barra lateral direita
    list_filter = ('tipo_usuario', 'is_staff', 'is_active')
    
    # --- Configuração da tela de EDIÇÃO de um usuário ---
    # Os 'fieldsets' organizam os campos em seções.
    # É importante garantir que TODOS os campos que queremos editar estejam aqui.
    fieldsets = (
        # Seção de Login e Dados Pessoais
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('email', 'telefone')}),
        # Nossa seção personalizada
        ('Dados Personalizados', {'fields': ('tipo_usuario',)}),
        # Seção de Permissões do Django
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        # Seção de Datas Importantes
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    
    # --- Configuração da tela de CRIAÇÃO de um usuário (a 1ª etapa) ---
    # Campos que aparecem na primeira tela de criação de usuário
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password', 'password2'), # password2 é o campo de confirmação
        }),
    )
    
    # Campos para busca na lista de usuários
    search_fields = ('email', 'username')
    # Ordem padrão da lista
    ordering = ('email',)

# Registra nosso model Usuario com nossa classe de admin customizada
admin.site.register(Usuario, CustomUserAdmin)