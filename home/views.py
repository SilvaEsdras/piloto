from django.shortcuts import render
from django.http import HttpResponse

# View da página inicial
def index(request):
    return render(request, 'index.html')

# View Sobre
def sobre(request):
    return render(request, 'sobre.html')

# View Contato
def contato(request):
    return render(request, 'contato.html')

# View Ajuda
def ajuda(request):
    return render(request, 'ajuda.html')

# --- Exercícios Anteriores (Mantidos) ---

def perfil(request, usuario):
    # Pode criar um perfil.html se quiser, ou retornar simples por enquanto
    return HttpResponse(f"<h1>Página de Perfil</h1><p>Esse é o perfil de {usuario}</p>")

def diasemana(request, dia):
    dias = {
        1: "Domingo",
        2: "Segunda-feira",
        3: "Terça-feira",
        4: "Quarta-feira",
        5: "Quinta-feira",
        6: "Sexta-feira",
        7: "Sábado"
    }
    dia_nome = dias.get(dia, "Dia inválido")
    contexto = {'dia_numero': dia, 'dia_nome': dia_nome}
    return render(request, 'diasemana.html', contexto)