from django.urls import path
from contas import views

app_name = 'contas'

urlpatterns = [
    path('', views.listar_alunos, name='lista-alunos'),
    path('cadastrar-aluno/', views.cadastrar_alunos, name='cadastrar-aluno'),
    path('altera-aluno/<int:aluno_id>/', views.alterar_aluno, name='altera-aluno'),
    path('excluir-aluno/<int:aluno_id>/', views.excluir_aluno, name='excluir-aluno')
]