from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sobre/', views.sobre, name='sobre'),
    path('contato/', views.contato, name='contato'),
    path('ajuda/', views.ajuda, name='ajuda'),
    
    # Exercício 1: Rota para o perfil do usuário [cite: 88]
    path('perfil/<str:usuario>/', views.perfil, name='perfil'),
    
    # Exercício 2: Rota para o dia da semana (recebe um inteiro) [cite: 95]
    path('diasemana/<int:dia>/', views.diasemana, name='diasemana'),
]