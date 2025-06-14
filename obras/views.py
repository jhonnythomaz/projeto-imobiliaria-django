# obras/views.py

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Obra

# O decorator @login_required garante que apenas usuários logados
# possam acessar esta página. Se um usuário não logado tentar acessar,
# ele será automaticamente redirecionado para a página de login.
@login_required 
def lista_obras(request):
    # 1. A Lógica: Buscar os dados no banco de dados.
    # Buscamos todos os objetos do nosso model 'Obra'.
    # O Django é inteligente, mas para buscas complexas como esta,
    # podemos otimizá-lo para ser mais rápido.
    # .select_related('imovel'): Pede ao Django para, na mesma consulta ao banco,
    # já trazer os dados do imóvel relacionado a cada obra.
    # .prefetch_related('historico_status'): Faz uma segunda busca otimizada para
    # pegar TODO o histórico de status de TODAS as obras de uma vez só.
    # Isso evita dezenas de pequenas buscas ao banco de dados dentro do template.
    todas_as_obras = Obra.objects.select_related("imovel").prefetch_related("historico_status").all()
    
    # 2. O Contexto: Preparamos um dicionário para enviar os dados para o template.
    # A chave 'obras' conterá a lista de objetos que buscamos.
    context = {
        'obras': todas_as_obras
    }
    
    # 3. A Renderização: Juntamos os dados com o template e retornamos a resposta HTML.
    # O Django vai procurar pelo arquivo 'obras/lista_obras.html'.
    return render(request, 'obras/lista_obras.html', context)