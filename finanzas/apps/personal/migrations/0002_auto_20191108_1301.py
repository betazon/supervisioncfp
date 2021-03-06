# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-11-08 13:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alumnos',
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
            ],
            options={
                'ordering': ['apellido'],
                'verbose_name_plural': 'Alumnos',
            },
        ),
        migrations.AlterModelOptions(
            name='agrupacion',
            options={'ordering': ['descripcion'], 'verbose_name_plural': 'Agrupaciones'},
        ),
        migrations.AlterModelOptions(
            name='ciudad',
            options={'ordering': ['descripcion'], 'verbose_name_plural': 'Ciudades'},
        ),
        migrations.AlterModelOptions(
            name='empleado',
            options={'verbose_name_plural': 'Empleados'},
        ),
        migrations.AlterModelOptions(
            name='escalafon',
            options={'ordering': ['descripcion'], 'verbose_name_plural': 'Escalafones'},
        ),
        migrations.AlterModelOptions(
            name='jerarquia',
            options={'ordering': ['descripcion'], 'verbose_name_plural': 'Jerarquias'},
        ),
        migrations.AlterModelOptions(
            name='persona',
            options={'ordering': ['apellido'], 'verbose_name_plural': 'Personas'},
        ),
        migrations.AlterModelOptions(
            name='seccion',
            options={'ordering': ['descripcion'], 'verbose_name_plural': 'Secciones'},
        ),
        migrations.AlterModelOptions(
            name='sexo',
            options={'ordering': ['descripcion'], 'verbose_name_plural': 'Sexos'},
        ),
        migrations.AlterModelOptions(
            name='tipo_empleado',
            options={'ordering': ['descripcion'], 'verbose_name_plural': 'Tipos de Empleados'},
        ),
        migrations.AddField(
            model_name='alumnos',
            name='ciudad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personal.Ciudad'),
        ),
    ]
