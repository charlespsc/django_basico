from django.http import HttpResponse

# Create your views here.


def home(request):
    return HttpResponse(
        "<h1>Olá, Mundo! Esta é a página principal da app core.</h1>"
    )
