from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContatoForm, ProdutoForm 

def index(request):
    return render(request, 'index.html')

def sobre(request):
    return render(request, 'sobre.html')

def ajuda(request):
    return render(request, 'ajuda.html')

def contato(request):
    form = ContatoForm()
    contexto = {
        'form': form,
    }
    return render(request, 'contato.html', contexto)


def produtos(request):
    contexto = {
        'lista': [
            {'id': 1, 'nome': 'Notebook', 'preco': '2.500,00'},
            {'id': 2, 'nome': 'Monitor', 'preco': '500,00'},
            {'id': 3, 'nome': 'Teclado', 'preco': '80,00'},
        ],
    }
    return render(request, 'produto/lista.html', contexto)

def form_produto(request):
    form = ProdutoForm()
    contexto = {
        'form': form
    }
    return render(request, 'produto/form.html', contexto)

def exibir_item(request, id):
    return HttpResponse(f"<h1>Exibindo Item: {id}</h1>")

def diasemana(request, dia):
    dias = {
        1: "Domingo", 2: "Segunda-feira", 3: "Terça-feira",
        4: "Quarta-feira", 5: "Quinta-feira", 6: "Sexta-feira", 7: "Sábado"
    }
    dia_nome = dias.get(dia, "Dia inválido")
    contexto = {'dia_numero': dia, 'dia_nome': dia_nome}
    return render(request, 'diasemana.html', contexto)

def perfil(request, usuario):
    return HttpResponse(f"<h1>Perfil: {usuario}</h1>")

def form_produto(request):
    form = ProdutoForm()
    contexto = {
        'form': form
    }
    return render(request, 'produto/form.html', contexto)