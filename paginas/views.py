from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Projetos
from .forms import ProjetoForm



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

def projetos(request):
    projetos  = {
            "projetos": Projetos.objects.all(),
        }
    return render(request, "projetos.html",projetos)

def novo_projeto(request):
    if request.method == "POST":
        form = ProjetoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/projetos/")
    else:
        form = ProjetoForm()
    return render(request, "novo_projeto.html",
                  {"form": form})
