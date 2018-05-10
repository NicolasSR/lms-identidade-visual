from django.db import models

# Create your models here.
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
