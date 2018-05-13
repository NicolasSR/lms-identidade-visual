from django.urls import path
from contas import views

app_name = 'contas'

urlpatterns = [
    path('lista-alunos/', views.listar_alunos, name='lista-alunos'),
    path('cadastrar-aluno/', views.cadastrar_alunos, name='cadastrar-aluno'),
    path('altera-aluno/<int:aluno_id>/', views.alterar_aluno, name='altera-aluno'),
    path('excluir-aluno/<int:aluno_id>/', views.excluir_aluno, name='excluir-aluno'),
    path('lista-coordenadores/', views.listar_coordenadores, name='lista-coordenadores'),
    path('cadastrar-coordenador/', views.cadastrar_coordenador, name='cadastrar-coordenador'),
    path('altera-coordenador/<int:coordenador_id>/', views.alterar_coordenador, name='altera-coordenador'),
    path('excluir-coordenador/<int:coordenador_id>/', views.excluir_coordenador, name='excluir-coordenador')
]