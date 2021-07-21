from django.contrib import admin

from .models import Cadastro 

@admin.register(Cadastro)
class CadastroAdmin(admin.ModelAdmin):
    list_display = ('sigla', 'nome', 'cidade', 'escudo')

