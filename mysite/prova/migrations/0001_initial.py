# Generated by Django 4.2.3 on 2023-08-04 00:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('matricula', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Diario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=50)),
                ('num_aulas', models.IntegerField()),
                ('ano', models.IntegerField()),
                ('semestre', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Disciplina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('carga_horaria', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Rendimento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nota1', models.IntegerField()),
                ('nota2', models.IntegerField()),
                ('num_faltas', models.IntegerField()),
                ('diario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='diario_rendimentos', to='prova.diario')),
            ],
        ),
        migrations.AddField(
            model_name='diario',
            name='disciplina',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='disciplina_diario', to='prova.disciplina'),
        ),
    ]
