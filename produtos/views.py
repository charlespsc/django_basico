from django.shortcuts import render
from django.http import HttpResponse
from .models import Produto


# Create your views here.


def ver_produto(request):
    if request.method == 'GET':
        return render(request, 'ver_produto.html', {'nome': 'Produto Exemplo'})
    elif request.method == 'POST':
        nome = request.POST.get('nome')
        preco = request.POST.get('preco')
        descricao = request.POST.get('descricao')
        estoque = request.POST.get('estoque')

        produto = Produto(
            nome=nome,
            preco=preco,
            descricao=descricao,
            estoque=estoque
        )
        produto.save()

        return HttpResponse(
            (
                f"<h1>Cadastro de Produtos</h1>"
                f"<p>O produto '{nome}' foi cadastrado com sucesso!</p>"
            )
        )


def inserir_produto(request):
    return HttpResponse(
        "<h1>Inserir Produto</h1>"
        "<p>Esta é a página para inserir um novo produto.</p>"
    )
