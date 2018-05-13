from django.db import models
from contas.models import Coordenador

class Curso(models.Model):
    nome = models.CharField('Nome', db_column='NOME', max_length=30)

class Disciplina(models.Model):
    nome = models.CharField('Nome', db_column='NOME', unique=True, max_length=30)
    data = models.DateTimeField('Data', db_column='DATA', blank=True, null=True)
    status = models.CharField('Status', db_column='STATUS', max_length=7, blank=True, null=True)
    plano_ensino = models.CharField('Plano de Ensino', db_column='PLANOENSINO', max_length=8000, blank=True, null=True)
    carga_horaria = models.SmallIntegerField('Carga Horária', db_column='CARGAHORARIA')
    competencias = models.CharField('Competencias', max_length=450, blank=True, null=True)
    habilidades = models.CharField('Habilidades', max_length=500, blank=True, null=True)
    ementa = models.CharField('Ementa', max_length=300, blank=True, null=True)
    conteudo_programatico = models.CharField('Conteúdo Programatico', db_column='CONTEUDOPROGRAMATICO', max_length=1000, blank=True, null=True)
    bibliografia_basica = models.CharField('Bibliografia Básica', max_length=700, db_column='BIBLIOGRAFIABASICA', blank=True, null=True)
    bibliografia_complementar = models.CharField('Bibliografia Complementar', max_length=700, db_column='Bibliografia Complementar', blank=True, null=True)
    percentual_pratico = models.IntegerField('Percentual Prático', db_column='PERCENTUALPRATICO', blank=True, null=True)
    percentual_teorico = models.IntegerField('Percentual Teórico', db_column='PERCENTUALTEORICO', blank=True, null=True)
    idcoordenador = models.ForeignKey(Coordenador, db_column='idcoordenador', blank=True, null=True, on_delete=True)

class Disciplinaofertada(models.Model):
    idcoordenador = models.ForeignKey(Coordenador, db_column='IdCoordenador', on_delete=True)
    dtiniciomatricula = models.DateField(blank=True, null=True)
    dtfimatricula = models.DateField(blank=True, null=True)
    iddisciplina = models.ForeignKey(Disciplina, db_column='IDDISCIPLINA', on_delete=True)
    idcurso = models.ForeignKey(Curso, db_column='IDCURSO', on_delete=True)
    ano = models.SmallIntegerField(db_column='ANO')
    semestre = models.IntegerField(db_column='SEMESTRE')
    turma = models.CharField(db_column='TURMA', max_length=1)
    idprofessor = models.IntegerField(db_column='IDPROFESSOR', blank=True, null=True)
    metodologia = models.CharField(db_column='METODOLOGIA', max_length=150, blank=True, null=True)
    recursos = models.CharField(db_column='RECURSOS', max_length=150, blank=True, null=True)
    criterio_avaliacao = models.CharField(db_column='CRITERIOAVALIACAO', max_length=60, blank=True, null=True)
    planode_aulas = models.CharField(db_column='PLANODEAULAS', max_length=500, blank=True, null=True)