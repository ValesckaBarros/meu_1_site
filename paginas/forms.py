from django import forms
from .models import Projetos


class ProjetoForm(forms.ModelForm):
    class Meta:
        model = Projetos
        fields = ["titulo", "descricao", "ano", "categoria"]
