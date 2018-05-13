from django.shortcuts import render, redirect
from restrito.models import Atividade
from contas.models import Professor

def cadastrar_atividade(request):
    if request.method == 'GET':
        return render(request, 'cadastro-atividade.html')
    else:
        atividade = Atividade(titulo=request.POST.get('titulo'), descricao=request.POST.get('descricao'),
                              conteudo=request.POST.get('conteudo'), tipo=request.POST.get('tipo'), extras=request.POST.get('extras'),
                              idprofessor=Professor.objects.get(id=1))
        if request.POST.get('id'):
            atividade.id = request.POST.get('id')
        atividade.save()
        return redirect('/restrito/lista-atividades')

def listar_atividades(request):
    return render(request, 'lista-atividades.html', {'atividades': Atividade.objects.all()})

def alterar_atividade(request, atividade_id):
    atividade = Atividade.objects.get(id=atividade_id)
    return render(request, 'cadastro-atividade.html', {'atividade': atividade})

def excluir_atividade(request, atividade_id):
    atividade = Atividade.objects.get(id=atividade_id)
    atividade.delete()
    return redirect('/restrito/lista-atividades')