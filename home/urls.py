from django.urls import path
from . import views

urlpatterns = [
    # Rota vazia '' refere-se à raiz deste app 
    path('', views.index, name='index'),
    
    # Rota para /sobre/ [cite: 3594]
    path('sobre/', views.sobre, name='sobre'),
    
    # Rotas para os exercícios de contato e ajuda
    path('contato/', views.contato, name='contato'),
    
    path('ajuda/', views.ajuda, name='ajuda'),
]