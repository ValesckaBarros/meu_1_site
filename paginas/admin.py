from django.contrib import admin
from .models import Projetos, Categoria


class ProjetoAdmin(admin.ModelAdmin):
    list_display = ["titulo", "ano", "categoria"]


admin.site.register(Projetos, ProjetoAdmin)
admin.site.register(Categoria)

