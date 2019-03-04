from django.db import models

class Formulario(models.Model):
    nome = models.CharField(max_length=30, blank=False)
    senha = models.CharField(max_length=6, blank=False)
    nome_de_usuario = models.CharField(max_length=10, blank=False)
    email = models.EmailField(max_length=50, null=True, blank=False)
    user = models.BooleanField('ADM', null=True, blank=False)


class Atualizacao_territorio(models.Model):
    data_de_inicio = models.DateTimeField('Data de Início')
    data_ultima_vez_trabalhado = models.DateTimeField('Data da última vez trabalhado', null=True)
    dirigente = models.CharField(max_length=30, blank=False)
    quadras = models.CharField(max_length=50, blank=False)
    data_de_termino = models.DateTimeField('Data de Término')