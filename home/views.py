from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContatoForm, ProdutoForm

# --- DADOS (Simulação de Banco de Dados) ---
DADOS_PRODUTOS = [
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
]

# --- VIEWS ---

def index(request):
    return render(request, 'index.html')

def sobre(request):
    return render(request, 'sobre.html')

def ajuda(request):
    return render(request, 'ajuda.html')

def contato(request):
    form = ContatoForm()
    contexto = {'form': form}
    return render(request, 'contato.html', contexto)

def produtos(request):
    contexto = {'lista': DADOS_PRODUTOS}
    return render(request, 'produto/lista.html', contexto)

# Esta é a view que estava faltando ou com erro
def form_produto(request):
    form = ProdutoForm()
    contexto = {'form': form}
    return render(request, 'produto/form.html', contexto)

def exibir_item(request, id):
    item_encontrado = None
    for produto in DADOS_PRODUTOS:
        if produto['id'] == id:
            item_encontrado = produto
            break
    contexto = {'item': item_encontrado, 'id': id}
    return render(request, 'exibir_item.html', contexto)

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