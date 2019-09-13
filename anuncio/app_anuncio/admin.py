from django.contrib import admin
from .models import *
# Register your models here.
class AnuncioAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'Titulo', 'preco', 'Anuncio',
                    'nome_contato', 'telefone', 'secao',
                    'tipo_anuncio')


admin.site.register(Anuncio,AnuncioAdmin)



