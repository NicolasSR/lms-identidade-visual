# Generated by Django 2.0.5 on 2018-05-12 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(db_column='LOGIN', max_length=15, verbose_name='Login')),
                ('senha', models.CharField(db_column='SENHA', max_length=8, verbose_name='Senha')),
                ('nome', models.CharField(db_column='NOME', max_length=45, verbose_name='Nome')),
                ('email', models.CharField(db_column='EMAIL', max_length=70, verbose_name='E-mail')),
                ('celular', models.CharField(db_column='CELULAR', max_length=15, verbose_name='Celular')),
                ('data_expiracao', models.DateTimeField(db_column='DTEXPIRACAO', null=True, verbose_name='Data Expiração')),
                ('ra', models.IntegerField(db_column='RA', verbose_name='RA')),
                ('foto', models.CharField(blank=True, db_column='FOTO', max_length=200, null=True, verbose_name='Foto')),
                ('data_nascimento', models.DateField(db_column='DTNASCIMENTO', verbose_name='Data Nascimento')),
                ('cpf', models.CharField(blank=True, max_length=20, null=True, verbose_name='CPF')),
            ],
        ),
        migrations.CreateModel(
            name='Coordenador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(db_column='LOGIN', max_length=15, verbose_name='Login')),
                ('senha', models.CharField(db_column='SENHA', max_length=8, verbose_name='Senha')),
                ('nome', models.CharField(db_column='NOME', max_length=45, verbose_name='Nome')),
                ('email', models.CharField(db_column='EMAIL', max_length=70, verbose_name='E-mail')),
                ('celular', models.CharField(db_column='CELULAR', max_length=15, verbose_name='Celular')),
                ('data_expiracao', models.DateField(blank=True, db_column='DTEXPIRACAO', null=True, verbose_name='Data Expiração')),
            ],
        ),
        migrations.CreateModel(
            name='Mensagem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assunto', models.CharField(db_column='ASSUNTO', max_length=60, verbose_name='Assunto')),
                ('referencia', models.CharField(db_column='REFERENCIA', max_length=40, verbose_name='Referência')),
                ('conteudo', models.CharField(db_column='CONTEUDO', max_length=200, verbose_name='Conteúdo')),
                ('status', models.CharField(db_column='STATUS', max_length=10, verbose_name='Status')),
                ('data_envio', models.DateTimeField(db_column='DTENVIO', verbose_name='Data Envio')),
                ('data_resposta', models.DateField(blank=True, db_column='DTRESPOSTA', null=True, verbose_name='Data Resposta')),
                ('resposta', models.CharField(blank=True, db_column='RESPOSTA', max_length=200, null=True, verbose_name='Resposta')),
                ('idaluno', models.ForeignKey(db_column='IDALUNO', on_delete=True, to='contas.Aluno')),
            ],
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(db_column='LOGIN', max_length=15, verbose_name='Login')),
                ('senha', models.CharField(db_column='SENHA', max_length=8, verbose_name='Senha')),
                ('nome', models.CharField(db_column='NOME', max_length=45, verbose_name='Nome')),
                ('email', models.CharField(db_column='EMAIL', max_length=70, verbose_name='E-mail')),
                ('celular', models.CharField(db_column='CELULAR', max_length=15, verbose_name='Celular')),
                ('data_expiracao', models.DateField(db_column='DTEXPIRACAO', verbose_name='Data Expiração')),
                ('apelido', models.CharField(db_column='APELIDO', max_length=20, verbose_name='Apelido')),
            ],
        ),
        migrations.AddField(
            model_name='mensagem',
            name='idprofessor',
            field=models.ForeignKey(db_column='IDPROFESSOR', on_delete=True, to='contas.Professor'),
        ),
    ]
