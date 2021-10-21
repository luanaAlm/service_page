from django.contrib import messages
from django.shortcuts import render
from .form import ClienteForm
from django.shortcuts import redirect, render


def index(request):
    form = ClienteForm()
    return render(request, "index.html", {
        "form": form
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
