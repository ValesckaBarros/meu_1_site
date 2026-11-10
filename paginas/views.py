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
    return render(request, "sobre.html")

def contato(request):
    dados  = {
            "email":"Valescka@email.com",
            "tel":819999999,
        }
    return render(request, "contatos.html",dados)
