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


