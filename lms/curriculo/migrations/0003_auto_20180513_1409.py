# Generated by Django 2.0.5 on 2018-05-13 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curriculo', '0002_auto_20180513_1346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disciplina',
            name='bibliografia_complementar',
            field=models.CharField(blank=True, db_column='BIBLIOGRAFIACOMPLEMENTAR', max_length=700, null=True, verbose_name='Bibliografia Complementar'),
        ),
    ]