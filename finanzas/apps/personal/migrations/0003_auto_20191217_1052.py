# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-12-17 10:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0002_auto_20191108_1301'),
    ]

    operations = [
        migrations.CreateModel(
            name='Asistencia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('estado', models.CharField(max_length=8)),
                ('alumnos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personal.Alumnos')),
            ],
            options={
                'ordering': ['alumnos'],
                'verbose_name_plural': 'Numero de centro',
            },
        ),
        migrations.CreateModel(
            name='Cfp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cue', models.CharField(max_length=15)),
                ('nombre', models.CharField(max_length=30)),
                ('director', models.CharField(max_length=30)),
                ('domicilio', models.CharField(max_length=30)),
                ('sede', models.CharField(max_length=2)),
                ('calificacion', models.CharField(max_length=2)),
            ],
            options={
                'ordering': ['nombre'],
                'verbose_name_plural': 'Numero de centro',
            },
        ),
        migrations.CreateModel(
            name='clases',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('alumnos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personal.Alumnos')),
                ('asistencia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personal.Asistencia')),
            ],
        ),
        migrations.CreateModel(
            name='Cursos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_ini', models.DateField()),
                ('fecha_fin', models.DateField()),
                ('sede', models.CharField(max_length=2)),
                ('desgranamiento', models.CharField(max_length=2)),
                ('cfp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personal.Cfp')),
            ],
        ),
        migrations.CreateModel(
            name='Docentes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apellido', models.CharField(max_length=30)),
                ('nombre', models.CharField(max_length=30)),
                ('documento', models.CharField(max_length=8)),
                ('telefono', models.CharField(max_length=11)),
                ('email', models.EmailField(max_length=254)),
                ('direccion', models.CharField(max_length=50)),
                ('fecha_nac', models.DateField()),
                ('lugar_nac', models.CharField(max_length=30)),
                ('ciudad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personal.Ciudad')),
            ],
            options={
                'ordering': ['apellido'],
                'verbose_name_plural': 'Docentes',
            },
        ),
        migrations.AddField(
            model_name='cursos',
            name='docente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personal.Docentes'),
        ),
        migrations.AddField(
            model_name='clases',
            name='cursos',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personal.Cursos'),
        ),
        migrations.AddField(
            model_name='asistencia',
            name='cursos',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personal.Cursos'),
        ),
    ]
