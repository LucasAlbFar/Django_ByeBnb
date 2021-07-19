from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('<int:cripto_id>', criptomoedas, name='criptomoedas'),
    path('busca', buscar, name='buscar'),
    path('inserir_cripto', inserir_cripto, name='inserir_cripto'),
    path('delete_cripto/<int:cripto_id>', delete_cripto, name='delete_cripto'),
    path('edit_cripto/<int:cripto_id>', edit_cripto, name='edit_cripto'),
    path('update_cripto', update_cripto, name='update_cripto'),
]
