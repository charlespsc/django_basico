from django.http import HttpResponse

# Create your views here.


def ver_produto(request):
    return HttpResponse(
        "<h1>Detalhes do Produto</h1>"
        "<p>Este é o produto que você está visualizando.</p>"
    )
