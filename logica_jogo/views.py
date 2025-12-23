from django.shortcuts import render, redirect
from tema_diario.models import TemaDiario
from espectro_cores.models import Cor


def home(request):
    return render(request, 'logica_jogo/home.html')


def jogo(request):
    tema = TemaDiario.objects.first()
    cores = Cor.objects.all()

    return render(request, 'logica_jogo/jogo.html', {
        'tema': tema,
        'cores': cores
    })


def resultado(request):
    if request.method == 'POST':
        cor_escolhida = request.POST.get('cor')
        tema_id = request.POST.get('tema')

        tema = TemaDiario.objects.get(id=tema_id)

        acertou = (cor_escolhida == tema.cor_correta.hex)

        return render(request, 'logica_jogo/resultado.html', {
            'tema': tema,
            'cor_escolhida': cor_escolhida,
            'acertou': acertou
        })

    return redirect('home')
