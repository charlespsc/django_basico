from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def ver_produto(request):
    return render(request, 'ver_produto.html', {'nome': 'Produto Exemplo'})


def inserir_produto(request):
    return HttpResponse(
        "<h1>Inserir Produto</h1>"
        "<p>Esta é a página para inserir um novo produto.</p>"
    )
