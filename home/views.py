from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

def sobre(request):
    return render(request, 'sobre.html')

def contato(request):
    return render(request, 'contato.html')

def ajuda(request):
    return render(request, 'ajuda.html')

# --- Nova View de Produtos com Lista Completa ---
def produtos(request):
    contexto = {
        'lista': [
            {'id': 1, 'nome': 'Notebook', 'preco': '2.500,00'},
            {'id': 2, 'nome': 'Monitor', 'preco': '500,00'},
            {'id': 3, 'nome': 'Teclado', 'preco': '80,00'},
            {'id': 4, 'nome': 'Mouse', 'preco': '40,00'},
            {'id': 5, 'nome': 'Impressora', 'preco': '600,00'},
            {'id': 6, 'nome': 'Scanner', 'preco': '700,00'},
            {'id': 7, 'nome': 'Câmera Web', 'preco': '150,00'},
            {'id': 8, 'nome': 'Headset', 'preco': '120,00'},
            {'id': 9, 'nome': 'Pendrive 32GB', 'preco': '30,00'},
            {'id': 10, 'nome': 'HD Externo 1TB', 'preco': '350,00'},
            {'id': 11, 'nome': 'Estabilizador', 'preco': '200,00'},
            {'id': 12, 'nome': 'Switch 8 portas', 'preco': '180,00'},
            {'id': 13, 'nome': 'Roteador Wi-Fi', 'preco': '220,00'},
        ],
    }
    return render(request, 'produto/lista.html', contexto)

# --- View para evitar erro no link 'Exibir Item' ---
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