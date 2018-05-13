from django.urls import path
from curriculo import views

app_name = 'curriculo'

urlpatterns = [
    path('lista-cursos/', views.listar_cursos, name='lista-cursos'),
    path('cadastrar-curso/', views.cadastrar_curso, name='cadastrar-curso'),
    path('altera-curso/<int:curso_id>/', views.alterar_curso, name='altera-curso'),
    path('excluir-curso/<int:curso_id>/', views.excluir_curso, name='excluir-curso')
]