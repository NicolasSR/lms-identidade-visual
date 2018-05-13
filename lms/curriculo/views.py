from django.shortcuts import render, redirect
from curriculo.models import Curso, Disciplina
from contas.models import Coordenador
from datetime import datetime

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

def cadastrar_disciplina(request):
    if request.method == 'GET':
        return render(request, 'cadastro-disciplina.html', {'coordenadores': Coordenador.objects.all()})
    else:
        disciplina = Disciplina(nome=request.POST.get('nome'), data=datetime.today(), status=request.POST.get('status'),
                                carga_horaria=request.POST.get('cargahoraria'), percentual_pratico=0,
                                percentual_teorico=0,
                                idcoordenador=Coordenador.objects.get(id=request.POST.get('coordenador')),
                                plano_ensino=request.POST.get('ensino'), competencias=request.POST.get('competencias'),
                                habilidades=request.POST.get('habilidades'), ementa=request.POST.get('ementa'),
                                conteudo_programatico=request.POST.get('conteudo'), bibliografia_basica=request.POST.get('basica'),
                                bibliografia_complementar=request.POST.get('complementar'))
        if request.POST.get('teorico'):
            disciplina.percentual_teorico = request.POST.get('teorico')
        if request.POST.get('pratico'):
            disciplina.percentual_pratico = request.POST.get('pratico')
        if request.POST.get('id'):
            disciplina.id = request.POST.get('id')
        disciplina.save()
        return redirect('/curriculo/lista-disciplinas')

def listar_disciplinas(request):
    return render(request, 'lista-disciplinas.html', {'disciplinas': Disciplina.objects.all()})

def alterar_disciplina(request, disciplina_id):
    disciplina = Disciplina.objects.get(id=disciplina_id)
    return render(request, 'cadastro-disciplina.html', {'disciplina': disciplina, 'coordenadores': Coordenador.objects.all()})

def excluir_disciplina(request, disciplina_id):
    disciplina = Disciplina.objects.get(id=disciplina_id)
    disciplina.delete()
    return redirect('/curriculo/lista-disciplinas')