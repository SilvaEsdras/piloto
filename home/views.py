from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    html_content = """
    <h1>Página Inicial</h1>
    <p>A view index funcionou, Wow!</p>
    <hr>
    <a href="/admin/"><button>Admin</button></a>
    <a href="/sobre/"><button>Sobre</button></a>
    <a href="/ajuda/"><button>Ajuda</button></a>
    <a href="/contato/"><button>Contato</button></a>
    """
    return HttpResponse(html_content)


def sobre(request):
    return HttpResponse("<h1>Sobre o Sistema</h1> <br> <a href='/'>Voltar</a>")


def contato(request):
    return HttpResponse("Esta é a página de contato. <br> <a href='/'>Voltar</a>")


def ajuda(request):
    return HttpResponse("Esta é a página de ajuda. <br> <a href='/'>Voltar</a>")