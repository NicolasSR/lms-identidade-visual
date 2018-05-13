from django.urls import path
from restrito import views

app_name = 'restrito'

urlpatterns = [
    path('lista-atividades', views.listar_atividades, name='lista-atividades'),
    path('cadastrar-atividade', views.cadastrar_atividade, name='cadastrar-atividade'),
    path('alterar-atividade/<int:atividade_id>', views.alterar_atividade, name='alterar-atividade'),
    path('excluir-atividade/<int:atividade_id>', views.excluir_atividade, name='excluir-atividade')
]