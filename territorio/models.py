from django.db import models

#Cara eu fiz esse model pra add user. Mas quero refatorar, creio que ele não é nescessário,
#visto que o django admin já faz tudo.
class Formulario(models.Model):
    nome = models.CharField(max_length=30, blank=False)
    senha = models.CharField(max_length=6, blank=False)
    nome_de_usuario = models.CharField(max_length=10, blank=False)
    email = models.EmailField(max_length=50, null=True, blank=False)
    user = models.BooleanField('ADM', null=True, blank=False)

    def __str__(self):
        return self.nome


class Atualizacao_territorio(models.Model):
    data_de_inicio = models.DateTimeField('Data de Início')
    data_ultima_vez_trabalhado = models.DateTimeField('Data da última vez trabalhado', null=True)
    dirigente = models.CharField(max_length=30, blank=False)
    quadras = models.CharField(max_length=50, blank=False)
    data_de_termino = models.DateTimeField('Data de Término')

    def __str__(self):
        return self.dirigente