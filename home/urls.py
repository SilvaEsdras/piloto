from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sobre/', views.sobre, name='sobre'),
    path('contato/', views.contato, name='contato'),
    path('ajuda/', views.ajuda, name='ajuda'),
    path('produto/', views.produtos, name='produto'),
    path('produto/form/', views.form_produto, name='form_produto'),
    path('exibir_item/<int:id>/', views.exibir_item, name='exibir_item'),
    path('diasemana/<int:dia>/', views.diasemana, name='diasemana'),
    path('perfil/<str:usuario>/', views.perfil, name='perfil'),
]