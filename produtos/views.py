from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def ver_produto(request):
    if request.method == 'GET':
        return render(request, 'ver_produto.html', {'nome': 'Produto Exemplo'})
    elif request.method == 'POST':
        nome = request.POST.get('nome')
        quantidade = request.POST.get('quantidade')

        return HttpResponse(
            (
                f"<h1>Cadastro de Produtos</h1>"
                f"<p>O produto '{nome}' (quantidade: {quantidade}) "
                "foi cadastrado com sucesso!</p>"
            )
        )


def inserir_produto(request):
    return HttpResponse(
        "<h1>Inserir Produto</h1>"
        "<p>Esta é a página para inserir um novo produto.</p>"
    )
