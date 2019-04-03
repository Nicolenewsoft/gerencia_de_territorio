from django.contrib import admin

from .models import Formulario, Atualizacao_territorio
#from django.contrib.auth.admin import UserAdmin

#UserAdmin.list_display = ('new_field',)  # don't forget the commas
#UserAdmin.list_filter = ('new_field', )
#UserAdmin.fieldsets = ('new_field',)

admin.site.register(Formulario)
admin.site.register(Atualizacao_territorio)