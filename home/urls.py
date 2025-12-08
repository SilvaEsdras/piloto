from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sobre/', views.sobre, name='sobre'),
    path('contato/', views.contato, name='contato'),
    path('ajuda/', views.ajuda, name='ajuda'),
    
    # Rota para produtos (Note que a view se chama 'produtos' mas o name é 'produto')
    path('produto/', views.produtos, name='produto'),
    
    # Rotas com parâmetros (exigidas pelo menu)
    path('exibir_item/<int:id>/', views.exibir_item, name='exibir_item'),
    path('diasemana/<int:dia>/', views.diasemana, name='diasemana'),
    path('perfil/<str:usuario>/', views.perfil, name='perfil'),
]