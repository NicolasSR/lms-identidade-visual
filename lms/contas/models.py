from django.db import models

class Aluno(models.Model):
    login = models.CharField('Login', db_column='LOGIN', max_length=15)
    senha = models.CharField('Senha', db_column='SENHA', max_length=8)
    nome = models.CharField('Nome', db_column='NOME', max_length=45)
    email = models.CharField('E-mail', db_column='EMAIL', max_length=70)
    celular = models.CharField('Celular', db_column='CELULAR', max_length=15)
    data_expiracao = models.DateTimeField('Data Expiração', db_column='DTEXPIRACAO', null=True)
    ra = models.IntegerField('RA', db_column='RA')
    foto = models.CharField('Foto', db_column='FOTO', max_length=200, blank=True, null=True)
    data_nascimento = models.DateField('Data Nascimento', db_column='DTNASCIMENTO')
    cpf = models.CharField('CPF', max_length=20, blank=True, null=True)

class Coordenador(models.Model):
    login = models.CharField('Login', db_column='LOGIN', max_length=15)
    senha = models.CharField('Senha', db_column='SENHA', max_length=8)
    nome = models.CharField('Nome', db_column='NOME', max_length=45)
    email = models.CharField('E-mail', db_column='EMAIL', max_length=70)
    celular = models.CharField('Celular', db_column='CELULAR', max_length=15)
    data_expiracao = models.DateField('Data Expiração', db_column='DTEXPIRACAO', blank=True, null=True)

class Professor(models.Model):
    login = models.CharField('Login', db_column='LOGIN', max_length=15)
    senha = models.CharField('Senha', db_column='SENHA', max_length=8)
    nome = models.CharField('Nome', db_column='NOME', max_length=45)
    email = models.CharField('E-mail', db_column='EMAIL', max_length=70)
    celular = models.CharField('Celular', db_column='CELULAR', max_length=15)
    data_expiracao = models.DateField('Data Expiração', db_column='DTEXPIRACAO')
    apelido = models.CharField('Apelido', db_column='APELIDO', max_length=20)

class Mensagem(models.Model):
    idaluno = models.ForeignKey(Aluno, db_column='IDALUNO', on_delete=True)
    idprofessor = models.ForeignKey(Professor, db_column='IDPROFESSOR', on_delete=True)
    assunto = models.CharField('Assunto', db_column='ASSUNTO', max_length=60)
    referencia = models.CharField('Referência', db_column='REFERENCIA', max_length=40)
    conteudo = models.CharField('Conteúdo', db_column='CONTEUDO', max_length=200)
    status = models.CharField('Status', db_column='STATUS', max_length=10)
    data_envio = models.DateTimeField('Data Envio', db_column='DTENVIO')
    data_resposta = models.DateField('Data Resposta', db_column='DTRESPOSTA', blank=True, null=True)
    resposta = models.CharField('Resposta', db_column='RESPOSTA', max_length=200, blank=True, null=True)