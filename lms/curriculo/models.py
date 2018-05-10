from django.db import models

# Create your models here.
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
