from django.shortcuts import render, redirect
from tema_diario.models import TemaDiario
from espectro_cores.models import Cor


def index(request):
    return render(request, 'logica_jogo/home.html')


def jogo(request):
    tema = TemaDiario.objects.order_by('-id').first()

    if not tema:
        return render(request, 'logica_jogo/no_tema.html')

    if request.method == "POST":
        cor_usuario = request.POST.get("cor")
        return redirect(f'/resultado/?tema={tema.id}&cor={cor_usuario}')

    cores = Cor.objects.all()
    return render(request, 'logica_jogo/jogo.html', {"tema": tema, "cores": cores})


def resultado(request):
    tema_id = request.GET.get("tema")
    cor_usuario = request.GET.get("cor")

    tema = TemaDiario.objects.get(id=tema_id)
    cor_correta = Cor.objects.first()

    return render(request, 'logica_jogo/resultado.html', {
        "tema": tema,
        "cor_usuario": cor_usuario,
        "cor_correta": cor_correta.hex if cor_correta else "#000000"
    })
