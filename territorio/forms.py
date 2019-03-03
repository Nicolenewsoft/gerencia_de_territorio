from django.forms import ModelForm
from .models import Formulario, Atualizacao_territorio
from django import forms


#Criar um formulário pegando os campos do model


class AddForm(ModelForm):
    class Meta:
        model = Formulario
        fields = ['nome', 'senha', 'nome_de_usuario', 'email', 'classificacao']

class Att_territorio(ModelForm):
    class Meta:
        model = Atualizacao_territorio
        fields = ['data_de_inicio', 'dirigente', 'quadras', 'data_de_termino']
        