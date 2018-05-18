from django.shortcuts import render, redirect
from curriculo.models import Curso, Disciplina, Disciplinaofertada
from contas.models import Coordenador, Professor
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

def cadastrar_disciplina_ofertada(request):
    if request.method == 'GET':
        cursos = Curso.objects.all()
        professores = Professor.objects.all()
        coordenadores = Coordenador.objects.all()
        disciplinas = Disciplina.objects.all()
        return render(request, 'cadastro-disciplina-ofertada.html', {'cursos': cursos,
                'professores': professores, 'coordenadores': coordenadores, 'disciplinas': disciplinas})
    else:        
        disciplina_ofertada = Disciplinaofertada(dtiniciomatricula=request.POST.get('datainicio'),
            dtfimatricula=request.POST.get('datafim'), ano=request.POST.get('ano'), 
            semestre=request.POST.get('semestre'), turma=request.POST.get('turma'), 
            metodologia=request.POST.get('metodologia'), recursos=request.POST.get('recursos'),
            criterio_avaliacao=request.POST.get('criterio'), planode_aulas=request.POST.get('planoaulas'),
            idprofessor=Professor.objects.get(id=request.POST.get('professor')),
            idcoordenador=Coordenador.objects.get(id=request.POST.get('coordenador')),
            idcurso = Curso.objects.get(id=request.POST.get('curso')),
            iddisciplina=Disciplina.objects.get(id=request.POST.get('disciplina')))
        if request.POST.get('id'):
            disciplina_ofertada.id = request.POST.get('id')
        disciplina_ofertada.save()
        return redirect('/curriculo/lista-disciplinas-ofertadas')

def listar_disciplinas_ofertadas(request):
    disciplinas_ofertadas = Disciplinaofertada.objects.all()
    return render(request, 'lista-disciplinas-ofertadas.html', 
        {'disciplinas_ofertadas': disciplinas_ofertadas})

def alterar_disciplina_ofertada(request, id):
    cursos = Curso.objects.all()
    professores = Professor.objects.all()
    coordenadores = Coordenador.objects.all()
    disciplinas = Disciplina.objects.all()
    disciplina_ofertada = Disciplinaofertada.objects.get(id=id)
    datainicio = str(disciplina_ofertada.dtiniciomatricula)
    datafim = str(disciplina_ofertada.dtfimatricula)
    return render(request, 'cadastro-disciplina-ofertada.html', {'disciplina_ofertada': disciplina_ofertada,
                'cursos': cursos, 'professores': professores, 'coordenadores': coordenadores, 
                'disciplinas': disciplinas, 'datainicio': datainicio, 'datafim': datafim})

def excluir_disciplina_ofertada(request, id):
    disciplina_ofertada = Disciplinaofertada.objects.get(id=id)
    disciplina_ofertada.delete()
    return redirect('/curriculo/lista-disciplinas-ofertadas')