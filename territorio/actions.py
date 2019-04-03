def territorio_finalizado(modeladmin, request, queryset):
    queryset.update(territorio_finalizado='True')

territorio_finalizado.short_description = "Território finalizado"

def territorio_nao_finalizado(modeladmin, request, queryset):
    queryset.update(territorio_nao_finalizado='False')

territorio_nao_finalizado.short_description = "Território não finalizado"