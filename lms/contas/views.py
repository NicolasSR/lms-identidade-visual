from django.shortcuts import render, redirect
from contas.models import Aluno

def cadastrar_alunos(request):
    if request.method == 'GET':
        return render(request, 'cadastro-aluno.html')
    else:
        id = 0
        if request.POST.get('id'):
            id = request.POST.get('id')
        aluno = Aluno(id=id, nome=request.POST.get('nome'), login=request.POST.get('login'), senha=request.POST.get('senha'),
                      email=request.POST.get('email'), celular=request.POST.get('celular'),
                      data_nascimento=request.POST.get('nascimento'),
                      cpf=request.POST.get('cpf'), ra=request.POST.get('ra'))
        aluno.save()
        return redirect('/contas')

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
    return redirect('/contas')