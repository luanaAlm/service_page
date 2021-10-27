from django.contrib import messages
from django.shortcuts import render
from .models import Portifolio
from .form import ClienteForm
from django.shortcuts import redirect, render


def index(request):
    portifolios = Portifolio.objects.all()
    form = ClienteForm()
    return render(request, "index.html", {
        "form": form, "portifolios": portifolios
    })


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
