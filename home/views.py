from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

# View criada nos slides anteriores
def index(request):
    return HttpResponse("A view index funcionou, Wow!")

# Exercício: Criar view 'sobre' com tag h1 [cite: 3591]
def sobre(request):
    return HttpResponse("<h1>Sobre o Sistema</h1>")

# Exercício: Criar view 'contato' [cite: 3597]
def contato(request):
    return HttpResponse("Esta é a página de contato.")

# Exercício: Criar view 'ajuda' [cite: 3599]
def ajuda(request):
    return HttpResponse("Esta é a página de ajuda.")