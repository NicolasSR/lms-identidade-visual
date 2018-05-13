from django.shortcuts import render, redirect
from curriculo.models import Curso

def cadastrar_curso(request):
    if request.method == 'GET':
        return render(request, 'cadastro-curso.html')
    else:
        if request.POST.get('id'):
            curso = Curso(id=request.POST.get('id'), nome=request.POST.get('nome'))
        else:
            curso = Curso(nome=request.POST.get('nome'))
        curso.save()
        return redirect('/curriculo/lista-cursos')

def listar_cursos(request):
    return render(request, 'lista-cursos.html', {'cursos': Curso.objects.all()})

def alterar_curso(request, curso_id):
    curso = Curso.objects.get(id=curso_id)
    return render(request, 'cadastro-curso.html', {'curso': curso})

def excluir_curso(request, curso_id):
    curso = Curso.objects.get(id=curso_id)
    curso.delete()
    return redirect('/curriculo/lista-cursos')
