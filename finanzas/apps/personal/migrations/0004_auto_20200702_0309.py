# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2020-07-02 03:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0003_auto_20191217_1052'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='asistencia',
            options={'ordering': ['alumnos'], 'verbose_name_plural': 'Asistencias'},
        ),
        migrations.AlterModelOptions(
            name='cfp',
            options={'ordering': ['nombre'], 'verbose_name_plural': 'Cfps'},
        ),
    ]
