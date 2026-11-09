from django.shortcuts import render
from django.http import HttpResponse

def inicio(request):
    dados  = {
        "nome":"Valescka",
        "idade":32,
        "altura": 1.7,
        "pets":["pipoca","mel"]
    }
    return render(request, "inicio.html",dados)

def sobre(request):
    return HttpResponse("<h1>Sobre mim</h1>"
                        "<p>Meu nome é valescka e estou aprendendo Django.</p>")

def contato(request):
    return HttpResponse(
        "<h1>Contato</h1>"
        "<p>E-mail: ana@email.com</p>"
        "<a href='/'>Início</a> | "
        "<a href='/sobre/'>Sobre</a>")
