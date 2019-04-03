from django.contrib import admin

from .models import Formulario, Atualizacao_territorio
from .actions import territorio_finalizado, territorio_nao_finalizado

class AtualizacaoTerritorioAdmin(admin.ModelAdmin):

    list_display = ('data_ultima_vez_trabalhado', 'dirigente', )
    actions = [territorio_finalizado, territorio_nao_finalizado]

admin.site.register(Formulario)
admin.site.register(Atualizacao_territorio, AtualizacaoTerritorioAdmin)