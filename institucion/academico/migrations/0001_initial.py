# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('id_estudiante', models.AutoField(serialize=False, primary_key=True)),
                ('nombre', models.CharField(max_length=50, null=True, blank=True)),
                ('apellido', models.CharField(max_length=50, null=True, blank=True)),
                ('dob', models.DateField(null=True, blank=True)),
                ('email', models.CharField(max_length=255, null=True, blank=True)),
                ('cedula', models.CharField(max_length=255, null=True, blank=True)),
            ],
            options={
                'db_table': 'estudiante',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Materia',
            fields=[
                ('id_materia', models.AutoField(serialize=False, primary_key=True)),
                ('nombre', models.CharField(max_length=50, null=True, blank=True)),
            ],
            options={
                'db_table': 'materia',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Paralelo',
            fields=[
                ('id_paralelo', models.AutoField(serialize=False, primary_key=True)),
                ('nombre', models.CharField(max_length=50, null=True, blank=True)),
            ],
            options={
                'db_table': 'paralelo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ParaleloEstudiante',
            fields=[
                ('id_paralelo_estudiante', models.AutoField(serialize=False, primary_key=True)),
            ],
            options={
                'db_table': 'paralelo_estudiante',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Periodo',
            fields=[
                ('id_periodo', models.AutoField(serialize=False, primary_key=True)),
                ('nombre', models.CharField(max_length=50, null=True, blank=True)),
            ],
            options={
                'db_table': 'periodo',
                'managed': False,
            },
        ),
    ]
