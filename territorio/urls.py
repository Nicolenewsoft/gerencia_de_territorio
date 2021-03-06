from django.urls import path
from .views import form, att, territorio_list, territorios_update, territorios_delete

urlpatterns = [
    path('form/', form, name="formulario"),
    path('att/', att, name= "atualizacao" ),
    path('territorio_list/', territorio_list, name="territorio_list" ),
    path('update/<int:id>/', territorios_update, name="territorios_update"),
    path('delete/<int:id>/', territorios_delete, name="territorios_delete")
]