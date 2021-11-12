from django.contrib import messages
from django.shortcuts import render
from .models import Portifolio
from .form import ClienteForm
from django.shortcuts import redirect, render


def index(request):
    #portifolios = Portifolio.objects.all()
    form = ClienteForm()
    return render(request, "index.html", {
        "form": form})


def cliente_novo(request):
    form = ClienteForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Sua mensagem foi enviada com sucesso!')
        return redirect('index')
    else:
        messages.error(
            request, 'Houve um erro, reenvie novamente a mensagem!')
        return redirect('index')


def landingPage(request):
    return render(request, "servicos/landing_page.html")


def siteInstitucional(request):
    return render(request, "servicos/site_institucional.html")


def lojaVirtual(request):
    return render(request, "servicos/loja_virtual.html")


def socialMedia(request):
    return render(request, "servicos/social_media.html")


def sobreNos(request):
    return render(request, "sobre_nos.html")


def Portifolio(request):
    return render(request, "portifolio.html")


def Duvidas(request):
    return render(request, "duvidas.html")


def Contato(request):
    return render(request, "contato.html")


def Orcamento(request):
    return render(request, "orcamento.html")
