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
    path('excluir-disciplina/<int:disciplina_id>/', views.excluir_disciplina, name='excluir-disciplina'),

    path('lista-disciplinas-ofertadas/', views.listar_disciplinas_ofertadas, name='lista-disciplinas-ofertadas'),
    path('cadastrar-disciplina-ofertada/', views.cadastrar_disciplina_ofertada, name='cadastrar-disciplina-ofertada'),
    path('altera-disciplina-ofertada/<int:id>/', views.alterar_disciplina_ofertada, name='altera-disciplina-ofertada'),
    path('excluir-disciplina-ofertada/<int:id>/', views.excluir_disciplina_ofertada, name='excluir-disciplina-ofertada')
]