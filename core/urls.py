from django.urls import path
from . import views  # Importa as views da nossa app 'core'

urlpatterns = [
    path('', views.home, name='home'),  # A URL raiz ('') chama a view 'home'
]
