# imoveis/views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Imovel, FotoImovel
from .forms import ImovelForm, FotoImovelForm

def lista_imoveis(request):
    imoveis_disponiveis = Imovel.objects.filter(disponivel=True).order_by('-data_cadastro')
    
    filtro_localizacao = request.GET.get('q_localizacao', '')
    filtro_tipo = request.GET.get('q_tipo', '')
    
    if filtro_localizacao:
        imoveis_disponiveis = imoveis_disponiveis.filter(localizacao__icontains=filtro_localizacao)
        
    if filtro_tipo:
        imoveis_disponiveis = imoveis_disponiveis.filter(tipo_imovel=filtro_tipo)
        
    context = {
        'imoveis': imoveis_disponiveis,
        'filtro_localizacao': filtro_localizacao,
        'filtro_tipo': filtro_tipo,
        'tipos_imovel': Imovel.TIPO_IMOVEL_CHOICES
    }
    
    return render(request, 'imoveis/lista_imoveis.html', context)

def detalhe_imovel(request, imovel_id):
    imovel = get_object_or_404(Imovel, pk=imovel_id)
    context = {
        'imovel': imovel
    }
    return render(request, 'imoveis/detalhe_imovel.html', context)

@login_required
def criar_imovel(request):
    if request.method == 'POST':
        form = ImovelForm(request.POST)
        if form.is_valid():
            imovel = form.save(commit=False)
            imovel.corretor_responsavel = request.user
            imovel.disponivel = True
            imovel.save()
            messages.success(request, 'Imóvel cadastrado com sucesso!')
            return redirect('imoveis:detalhe_imovel', imovel_id=imovel.id)
    else:
        form = ImovelForm()
    
    context = {
        'form': form
    }
    return render(request, 'imoveis/criar_imovel.html', context)

@login_required
def editar_imovel(request, imovel_id):
    imovel = get_object_or_404(Imovel, pk=imovel_id)
    
    if imovel.corretor_responsavel != request.user:
        messages.error(request, 'Você não tem permissão para editar este imóvel.')
        return redirect('imoveis:lista_imoveis')
        
    if request.method == 'POST':
        if 'salvar_dados_imovel' in request.POST:
            form_imovel = ImovelForm(request.POST, instance=imovel)
            if form_imovel.is_valid():
                form_imovel.save()
                messages.success(request, 'Dados do imóvel atualizados com sucesso!')
                return redirect('imoveis:editar_imovel', imovel_id=imovel.id)
        
        elif 'adicionar_foto' in request.POST:
            form_foto = FotoImovelForm(request.POST, request.FILES)
            if form_foto.is_valid():
                foto = form_foto.save(commit=False)
                foto.imovel = imovel
                foto.save()
                messages.success(request, 'Foto adicionada com sucesso!')
                return redirect('imoveis:editar_imovel', imovel_id=imovel.id)
    
    form_imovel = ImovelForm(instance=imovel)
    form_foto = FotoImovelForm()
    
    context = {
        'form_imovel': form_imovel,
        'form_foto': form_foto,
        'imovel': imovel
    }
    return render(request, 'imoveis/editar_imovel.html', context)