from django.urls import path
from . import views  # Importa as views da nossa app 'produtos'


urlpatterns = [
    path('ver_produto/', views.ver_produto, name='ver_produto'),
    path('inserir_produto/', views.inserir_produto, name='inserir_produto'),
]
