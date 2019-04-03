from django.contrib import admin

from .models import Formulario, Atualizacao_territorio

class AtualizacaoTerritorioAdmin(admin.ModelAdmin):

    list_display = ('data_ultima_vez_trabalhado', 'dirigente', )

admin.site.register(Formulario)
admin.site.register(Atualizacao_territorio, AtualizacaoTerritorioAdmin)