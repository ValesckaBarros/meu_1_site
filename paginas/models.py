from django.db import models

class Livro(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    ano = models.IntegerField()
    autor = models.CharField(max_length=100)
    genero = models.CharField(max_length=50) 

class Projetos(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    ano = models.IntegerField()
    