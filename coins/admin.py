from django.contrib import admin
from .models import Cripto

class ListagemCripto(admin.ModelAdmin):
    list_display = ('id', 'cripto_name', 'cripto_symbol', 'cripto_pessoa','cripto_published')
    list_display_links = ('id','cripto_name', 'cripto_symbol', 'cripto_pessoa')
    search_fields = ('cripto_name',)
    list_filter = ('cripto_category', )
    list_editable = ('cripto_published',)
    list_per_page = 10


admin.site.register(Cripto, ListagemCripto)

