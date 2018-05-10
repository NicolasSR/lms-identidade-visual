# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Aluno(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    login = models.CharField(db_column='LOGIN', unique=True, max_length=15)  # Field name made lowercase.
    senha = models.CharField(db_column='SENHA', max_length=8)  # Field name made lowercase.
    nome = models.CharField(db_column='NOME', max_length=45)  # Field name made lowercase.
    email = models.CharField(db_column='EMAIL', unique=True, max_length=70)  # Field name made lowercase.
    celular = models.CharField(db_column='CELULAR', unique=True, max_length=15)  # Field name made lowercase.
    dtexpiracao = models.DateTimeField(db_column='DTEXPIRACAO', blank=True, null=True)  # Field name made lowercase.
    ra = models.IntegerField(db_column='RA')  # Field name made lowercase.
    foto = models.CharField(db_column='FOTO', max_length=200, blank=True, null=True)  # Field name made lowercase.
    datanascimento = models.DateField()
    cpf = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'aluno'


class Atividade(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    titulo = models.CharField(db_column='TITULO', unique=True, max_length=30)  # Field name made lowercase.
    descricao = models.CharField(db_column='DESCRICAO', max_length=60, blank=True, null=True)  # Field name made lowercase.
    conteudo = models.CharField(db_column='CONTEUDO', max_length=200, blank=True, null=True)  # Field name made lowercase.
    tipo = models.CharField(db_column='TIPO', max_length=18, blank=True, null=True)  # Field name made lowercase.
    extras = models.CharField(db_column='EXTRAS', max_length=180, blank=True, null=True)  # Field name made lowercase.
    idprofessor = models.ForeignKey('Professor', models.DO_NOTHING, db_column='IDPROFESSOR')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'atividade'


class Atividadevinculada(models.Model):
    id = models.ForeignKey(Atividade, models.DO_NOTHING, db_column='ID', primary_key=True)  # Field name made lowercase.
    idatividade = models.IntegerField(db_column='IDATIVIDADE')  # Field name made lowercase.
    idprofessor = models.ForeignKey('Professor', models.DO_NOTHING, db_column='IDPROFESSOR')  # Field name made lowercase.
    iddisciplinaofertada = models.ForeignKey('Disciplinaofertada', models.DO_NOTHING, db_column='IDDISCIPLINAOFERTADA')  # Field name made lowercase.
    rotulo = models.CharField(db_column='ROTULO', max_length=5)  # Field name made lowercase.
    status = models.CharField(db_column='STATUS', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'atividadevinculada'
        unique_together = (('idatividade', 'iddisciplinaofertada', 'rotulo'),)


class Coordenador(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    login = models.CharField(db_column='LOGIN', unique=True, max_length=15)  # Field name made lowercase.
    senha = models.CharField(db_column='SENHA', max_length=8)  # Field name made lowercase.
    nome = models.CharField(db_column='NOME', max_length=45)  # Field name made lowercase.
    email = models.CharField(db_column='EMAIL', unique=True, max_length=70)  # Field name made lowercase.
    celular = models.CharField(db_column='CELULAR', unique=True, max_length=15)  # Field name made lowercase.
    dtexpiracao = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'coordenador'


class Curso(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nome = models.CharField(db_column='NOME', unique=True, max_length=30)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'curso'


class Disciplina(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nome = models.CharField(db_column='NOME', unique=True, max_length=30)  # Field name made lowercase.
    data = models.DateTimeField(db_column='DATA', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='STATUS', max_length=7, blank=True, null=True)  # Field name made lowercase.
    planodeensino = models.CharField(max_length=8000, blank=True, null=True)
    cargahoraria = models.SmallIntegerField(db_column='CARGAHORARIA')  # Field name made lowercase.
    competencias = models.CharField(max_length=450, blank=True, null=True)
    habilidades = models.CharField(max_length=500, blank=True, null=True)
    ementa = models.CharField(max_length=300, blank=True, null=True)
    conteudoprogramatico = models.CharField(max_length=1000, blank=True, null=True)
    bibliografiabasica = models.CharField(max_length=700, blank=True, null=True)
    bibliografiacomplementar = models.CharField(max_length=700, blank=True, null=True)
    percentualpratico = models.IntegerField(db_column='PERCENTUALPRATICO', blank=True, null=True)  # Field name made lowercase.
    percentualteorico = models.IntegerField(db_column='PERCENTUALTEORICO', blank=True, null=True)  # Field name made lowercase.
    idcoordenador = models.ForeignKey(Coordenador, models.DO_NOTHING, db_column='idcoordenador', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'disciplina'


class Disciplinaofertada(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    idcoordenador = models.ForeignKey(Coordenador, models.DO_NOTHING, db_column='IdCoordenador')  # Field name made lowercase.
    dtiniciomatricula = models.DateField(blank=True, null=True)
    dtfimatricula = models.DateField(blank=True, null=True)
    iddisciplina = models.ForeignKey(Disciplina, models.DO_NOTHING, db_column='IDDISCIPLINA')  # Field name made lowercase.
    idcurso = models.ForeignKey(Curso, models.DO_NOTHING, db_column='IDCURSO')  # Field name made lowercase.
    ano = models.SmallIntegerField(db_column='ANO')  # Field name made lowercase.
    semestre = models.IntegerField(db_column='SEMESTRE')  # Field name made lowercase.
    turma = models.CharField(db_column='TURMA', max_length=1)  # Field name made lowercase.
    idprofessor = models.IntegerField(db_column='IDPROFESSOR', blank=True, null=True)  # Field name made lowercase.
    metodologia = models.CharField(db_column='METODOLOGIA', max_length=150, blank=True, null=True)  # Field name made lowercase.
    recursos = models.CharField(db_column='RECURSOS', max_length=150, blank=True, null=True)  # Field name made lowercase.
    criterioavaliacao = models.CharField(db_column='CRITERIOAVALIACAO', max_length=60, blank=True, null=True)  # Field name made lowercase.
    planodeaulas = models.CharField(db_column='PLANODEAULAS', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'disciplinaofertada'


class Entrega(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    idaluno = models.ForeignKey(Aluno, models.DO_NOTHING, db_column='IDALUNO', unique=True)  # Field name made lowercase.
    idatividadevinculada = models.ForeignKey(Atividadevinculada, models.DO_NOTHING, db_column='IDATIVIDADEVINCULADA')  # Field name made lowercase.
    titulo = models.CharField(db_column='TITULO', max_length=30)  # Field name made lowercase.
    resposta = models.CharField(db_column='RESPOSTA', max_length=200)  # Field name made lowercase.
    dtentrega = models.DateTimeField(db_column='DTENTREGA')  # Field name made lowercase.
    status = models.CharField(db_column='STATUS', max_length=15)  # Field name made lowercase.
    idprofessor = models.IntegerField(db_column='IDPROFESSOR', blank=True, null=True)  # Field name made lowercase.
    nota = models.SmallIntegerField(db_column='NOTA', blank=True, null=True)  # Field name made lowercase.
    dtavaliacao = models.DateField(db_column='DTAVALIACAO', blank=True, null=True)  # Field name made lowercase.
    obs = models.CharField(db_column='OBS', max_length=90, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'entrega'


class Mensagem(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    idaluno = models.ForeignKey(Aluno, models.DO_NOTHING, db_column='IDALUNO')  # Field name made lowercase.
    idprofessor = models.ForeignKey('Professor', models.DO_NOTHING, db_column='IDPROFESSOR')  # Field name made lowercase.
    assunto = models.CharField(db_column='ASSUNTO', max_length=60)  # Field name made lowercase.
    referencia = models.CharField(db_column='REFERENCIA', max_length=40)  # Field name made lowercase.
    conteudo = models.CharField(db_column='CONTEUDO', max_length=200)  # Field name made lowercase.
    status = models.CharField(db_column='STATUS', unique=True, max_length=10)  # Field name made lowercase.
    dtenvio = models.DateTimeField(db_column='DTENVIO')  # Field name made lowercase.
    dtresposta = models.DateField(db_column='DTRESPOSTA', blank=True, null=True)  # Field name made lowercase.
    resposta = models.CharField(db_column='RESPOSTA', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mensagem'


class Professor(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    login = models.CharField(db_column='LOGIN', unique=True, max_length=15)  # Field name made lowercase.
    senha = models.CharField(db_column='SENHA', max_length=8)  # Field name made lowercase.
    nome = models.CharField(db_column='NOME', max_length=45)  # Field name made lowercase.
    email = models.CharField(db_column='EMAIL', unique=True, max_length=70)  # Field name made lowercase.
    celular = models.CharField(db_column='CELULAR', unique=True, max_length=15)  # Field name made lowercase.
    dtexpiracao = models.DateField(db_column='DTEXPIRACAO')  # Field name made lowercase.
    apelido = models.CharField(db_column='APELIDO', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'professor'


class Solicitacaomatricula(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    idaluno = models.ForeignKey(Aluno, models.DO_NOTHING, db_column='IDALUNO')  # Field name made lowercase.
    iddisciplinaofertada = models.ForeignKey(Disciplinaofertada, models.DO_NOTHING, db_column='IDDISCIPLINAOFERTADA')  # Field name made lowercase.
    dtsolicitacao = models.DateTimeField(db_column='DTSOLICITACAO')  # Field name made lowercase.
    idcoordenador = models.ForeignKey(Coordenador, models.DO_NOTHING, db_column='IDCOORDENADOR', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='STATUS', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'solicitacaomatricula'
