from django.urls import path
from . import views  # Importa as views da nossa app 'produtos'


urlpatterns = [
    path('ver_produto/', views.ver_produto, name='ver_produto'),
]
