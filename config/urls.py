# config/urls.py - VERSÃO ATUALIZADA

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# --- 1. IMPORTAMOS A NOSSA NOVA VIEW DE CADASTRO ---
from usuarios.views import SignUpView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('obras/', include('obras.urls')),
    
    # --- 2. ADICIONAMOS A NOVA URL DE CADASTRO ---
    # Ela vem ANTES do include de autenticação padrão.
    path('contas/signup/', SignUpView.as_view(), name='signup'),
    
    # URLs de Autenticação Padrão (Login, Logout, Recuperação de Senha)
    path('contas/', include('django.contrib.auth.urls')),
    
    # URL Principal do Site
    path('', include('imoveis.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)