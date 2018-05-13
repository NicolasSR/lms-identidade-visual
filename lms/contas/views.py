from django.shortcuts import render, redirect
from contas.models import Aluno, Coordenador, Professor

def cadastrar_alunos(request):
    if request.method == 'GET':
        return render(request, 'cadastro-aluno.html')
    else:
        if request.POST.get('id'):
            aluno = Aluno(id=request.POST.get('id'), nome=request.POST.get('nome'), login=request.POST.get('login'),
                          senha=request.POST.get('senha'),
                          email=request.POST.get('email'), celular=request.POST.get('celular'),
                          data_nascimento=request.POST.get('nascimento'),
                          cpf=request.POST.get('cpf'), ra=request.POST.get('ra'))
            aluno.save()
        else:
            aluno = Aluno(nome=request.POST.get('nome'), login=request.POST.get('login'),
                          senha=request.POST.get('senha'),
                          email=request.POST.get('email'), celular=request.POST.get('celular'),
                          data_nascimento=request.POST.get('nascimento'),
                          cpf=request.POST.get('cpf'), ra=request.POST.get('ra'))
            aluno.save()
        return redirect('/contas/lista-alunos')

def listar_alunos(request):
    return render(request, 'lista-alunos.html', {'alunos': Aluno.objects.all()})

def alterar_aluno(request, aluno_id):
    aluno = Aluno.objects.get(id=aluno_id)
    data = str(aluno.data_nascimento)
    print(data)
    return render(request, 'cadastro-aluno.html', {'aluno': aluno, 'nascimento': data})

def excluir_aluno(request, aluno_id):
    aluno = Aluno.objects.get(id=aluno_id)
    aluno.delete()
    return redirect('/contas/lista-alunos')

def cadastrar_coordenador(request):
    if request.method == 'GET':
        return render(request, 'cadastro-coordenador.html')
    else:
        if request.POST.get('id'):
            coordenador = Coordenador(id=request.POST.get('id'), login=request.POST.get('login'), senha=request.POST.get('senha'), nome=request.POST.get('nome'),
                                  email=request.POST.get('email'), celular=request.POST.get('celular'))
            coordenador.save()
        else:
            coordenador = Coordenador(login=request.POST.get('login'), senha=request.POST.get('senha'), nome=request.POST.get('nome'),
                                  email=request.POST.get('email'), celular=request.POST.get('celular'))
            coordenador.save()
        return redirect('/contas/lista-coordenadores')

def listar_coordenadores(request):
    return render(request, 'lista-coordenadores.html', {'coordenadores': Coordenador.objects.all()})

def alterar_coordenador(request, coordenador_id):
    coordenador = Coordenador.objects.get(id=coordenador_id)
    return render(request, 'cadastro-coordenador.html', {'coordenador': coordenador})

def excluir_coordenador(request, coordenador_id):
    coordenador = Coordenador.objects.get(id=coordenador_id)
    coordenador.delete()
    return redirect('/contas/lista-coordenadores')

def cadastrar_professor(request):
    if request.method == 'GET':
        return render(request, 'cadastro-professor.html')
    else:
        if request.POST.get('id'):
            professor = Professor(id=request.POST.get('id'), login=request.POST.get('login'), nome=request.POST.get('nome'),
                                    senha=request.POST.get('senha'), email=request.POST.get('email'), celular=request.POST.get('celular'),
                                    apelido=request.POST.get('apelido'))
            professor.save()
        else:
            professor = Professor(login=request.POST.get('login'), nome=request.POST.get('nome'),
                                    senha=request.POST.get('senha'), email=request.POST.get('email'), celular=request.POST.get('celular'),
                                    apelido=request.POST.get('apelido'))
            professor.save()
        return redirect('/contas/lista-professores')

def listar_professores(request):
    return render(request, 'lista-professores.html', {'professores': Professor.objects.all()})

def alterar_professor(request, professor_id):
    professor = Professor.objects.get(id=professor_id)
    return render(request, 'cadastro-professor.html', {'professor': professor})

def excluir_professor(request, professor_id):
    professor = Professor.objects.get(id=professor_id)
    professor.delete()
    return redirect('/contas/lista-professores')