from django.db import models
from contas.models import Aluno, Coordenador, Professor
from curriculo.models import Disciplinaofertada

class Solicitacaomatricula(models.Model):
    idaluno = models.ForeignKey(Aluno, db_column='IDALUNO', on_delete=True)
    iddisciplinaofertada = models.ForeignKey(Disciplinaofertada, db_column='IDDISCIPLINAOFERTADA', on_delete=True)
    dtsolicitacao = models.DateTimeField(db_column='DTSOLICITACAO')
    idcoordenador = models.ForeignKey(Coordenador, db_column='IDCOORDENADOR', blank=True, null=True, on_delete=True)
    status = models.CharField(db_column='STATUS', max_length=10, blank=True, null=True)

class Atividade(models.Model):
    titulo = models.CharField(db_column='TITULO', unique=True, max_length=30)
    descricao = models.CharField(db_column='DESCRICAO', max_length=60, blank=True, null=True)
    conteudo = models.CharField(db_column='CONTEUDO', max_length=200, blank=True, null=True)
    tipo = models.CharField(db_column='TIPO', max_length=18, blank=True, null=True)
    extras = models.CharField(db_column='EXTRAS', max_length=180, blank=True, null=True)
    idprofessor = models.ForeignKey(Professor, db_column='IDPROFESSOR', on_delete=True)

class Atividadevinculada(models.Model):
    idatividade = models.IntegerField(db_column='IDATIVIDADE')
    idprofessor = models.ForeignKey(Professor, db_column='IDPROFESSOR', on_delete=True)
    iddisciplinaofertada = models.ForeignKey(Disciplinaofertada, db_column='IDDISCIPLINAOFERTADA', on_delete=True)
    rotulo = models.CharField(db_column='ROTULO', max_length=5)
    status = models.CharField(db_column='STATUS', max_length=20)

class Entrega(models.Model):
    idaluno = models.ForeignKey(Aluno, db_column='IDALUNO', unique=True, on_delete=True)
    idatividadevinculada = models.ForeignKey(Atividadevinculada, db_column='IDATIVIDADEVINCULADA', on_delete=True)
    titulo = models.CharField(db_column='TITULO', max_length=30)
    resposta = models.CharField(db_column='RESPOSTA', max_length=200)
    dtentrega = models.DateTimeField(db_column='DTENTREGA')
    status = models.CharField(db_column='STATUS', max_length=15)
    idprofessor = models.IntegerField(db_column='IDPROFESSOR', blank=True, null=True)
    nota = models.SmallIntegerField(db_column='NOTA', blank=True, null=True)
    dtavaliacao = models.DateField(db_column='DTAVALIACAO', blank=True, null=True)
    obs = models.CharField(db_column='OBS', max_length=90, blank=True, null=True)