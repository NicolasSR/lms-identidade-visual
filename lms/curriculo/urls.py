from django.urls import path
from curriculo import views

app_name = 'curriculo'

urlpatterns = [
    path('lista-cursos/', views.listar_cursos, name='lista-cursos'),
    path('cadastrar-curso/', views.cadastrar_curso, name='cadastrar-curso'),
    path('altera-curso/<int:curso_id>/', views.alterar_curso, name='altera-curso'),
    path('excluir-curso/<int:curso_id>/', views.excluir_curso, name='excluir-curso'),

    path('lista-disciplinas/', views.listar_disciplinas, name='lista-disciplinas'),
    path('cadastrar-disciplina/', views.cadastrar_disciplina, name='cadastrar-disciplina'),
    path('altera-disciplina/<int:disciplina_id>/', views.alterar_disciplina, name='altera-disciplina'),
    path('excluir-disciplina/<int:disciplina_id>/', views.excluir_disciplina, name='excluir-disciplina')
]