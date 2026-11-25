from django.shortcuts import render, redirect, get_object_or_404
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
            "email":"xxxxxxxxxxxxx",
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


def detalhe_projeto(request, id):
    projeto = get_object_or_404(Projetos, id=id)
    return render(request, "detalhe_projeto.html",{"projeto":projeto}) 

def editar_projeto(request, id):
    projeto = get_object_or_404(Projetos, id=id)
    if request.method == "POST":
        form = ProjetoForm(request.POST, instance=projeto)
        if form.is_valid():
            form.save()
            return redirect("/projetos/")
    else:
        form = ProjetoForm(instance=projeto)
    return render(request, "novo_projeto.html", {"form": form})


def excluir_projeto(request, id):
    projeto = get_object_or_404(Projetos, id=id)
    if request.method == "POST":
        projeto.delete()
        return redirect("/projetos/")
    return render(request, "excluir_projeto.html",{"projeto": projeto})