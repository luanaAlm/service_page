from django.contrib import messages
from django.shortcuts import render
from .models import Depoimento, Portifolio_cliente, Social_Media
from .form import ClienteForm
from django.shortcuts import redirect, render


def index(request):
    port = Portifolio_cliente.objects.all()
    depoimento = Depoimento.objects.all()
    return render(request, "index.html", {
        "port": port,
        "depoimento": depoimento,
    })


def landingPage(request):
    text = 'Landing Page'
    subtext = 'Conquiste mais cliente e venda mais produtos ou serviços da sua empresa.'
    return render(request, "servicos/landing_page.html", {
        "text": text,
        "subtext": subtext
    })


def siteInstitucional(request):
    return render(request, "servicos/site_institucional.html")


def lojaVirtual(request):
    return render(request, "servicos/loja_virtual.html")


def seo(request):
    return render(request, "servicos/seo.html")


def socialMedia(request):
    return render(request, "servicos/social_media.html")


def sobreNos(request):
    return render(request, "sobre_nos.html")


def Portifolio(request):
    port2 = Portifolio_cliente.objects.all()
    socialMedia = Social_Media.objects.all()
    return render(request, "portifolio.html", {
        "port2": port2, "socialMedia": socialMedia
    })


def Duvidas(request):
    return render(request, "duvidas.html")


def Contato(request):
    form = ClienteForm()
    return render(request, "contato.html", {
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


def Orcamento(request):
    return render(request, "orcamento.html")
