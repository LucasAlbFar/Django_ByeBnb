from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from coins.models import Cripto
from django.contrib.auth.models import User
from django.contrib import auth, messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def index(request):
    moedas = Cripto.objects.order_by('-cripto_date_insert').filter(cripto_published=True)
    paginator = Paginator(moedas, 6)
    page = request.GET.get('page')
    moedas_por_pagina = paginator.get_page(page)
    dados = {
        'criptos': moedas_por_pagina
    }
    return render(request, 'criptos/index.html', dados)


def criptomoedas(request, cripto_id):
    cripto_pk = get_object_or_404(Cripto, pk=cripto_id)
    cripto_show = {
        'cripto' : cripto_pk
    }
    return render(request, 'criptos/criptomoedas.html', cripto_show)


def buscar(request):
    lista_moedas = Cripto.objects.order_by('-cripto_date_insert').filter(cripto_published=True)

    if 'buscar' in request.GET:
        nome_buscar = request.GET['buscar']

        if buscar:
            lista_moedas = lista_moedas.filter(cripto_name__icontains=nome_buscar)

    dados = {
        'criptos': lista_moedas
    }
    return render(request, 'criptos/buscar.html', dados)


def inserir_cripto(request):
    if request.method == 'POST':
        cripto_name = request.POST['cripto_name']
        cripto_creators = request.POST['cripto_creators']
        cripto_value = request.POST['cripto_value']
        cripto_symbol = request.POST['cripto_symbol']
        cripto_supply = request.POST['cripto_supply']
        cripto_description = request.POST['cripto_description']
        cripto_category = request.POST['cripto_category']
        crito_image = request.FILES['crito_image']

        user = get_object_or_404(User, pk=request.user.id)
        cripto = Cripto.objects.create(
            cripto_pessoa=user,
            cripto_name=cripto_name,
            cripto_creators=cripto_creators,
            cripto_value=cripto_value,
            cripto_symbol=cripto_symbol,
            cripto_supply=cripto_supply,
            cripto_description=cripto_description,
            cripto_category=cripto_category,
            crito_image=crito_image
        )
        cripto.save()
        return redirect('dashboard')
    else:
        return render(request, 'criptos/inserir_cripto.html')


def delete_cripto(request, cripto_id):
    cripto = get_object_or_404(Cripto, pk=cripto_id)
    cripto.delete()
    return redirect('dashboard')


def edit_cripto(request, cripto_id):
    cripto_pk = get_object_or_404(Cripto, pk=cripto_id)
    cripto_edit = {
        'cripto' : cripto_pk
    }
    return render(request,'criptos/edit_cripto.html', cripto_edit)


def update_cripto(request):
    if request.method == 'POST':
        cripto_id = request.POST['cripto_id']
        c = Cripto.objects.get(pk=cripto_id)
        c.cripto_name = request.POST['cripto_name']
        c.cripto_creators = request.POST['cripto_creators']
        c.cripto_value = request.POST['cripto_value']
        c.cripto_symbol = request.POST['cripto_symbol']
        c.cripto_supply = request.POST['cripto_supply']
        c.cripto_description = request.POST['cripto_description']
        c.cripto_category = request.POST['cripto_category']

        if 'crito_image' in request.FILES:
            c.crito_image = request.FILES['crito_image']

        c.save()
        return redirect('dashboard')