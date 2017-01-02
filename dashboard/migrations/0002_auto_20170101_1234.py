# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-01 12:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Buckminster1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temp', models.FloatField()),
                ('lux', models.FloatField()),
                ('rel_humidity', models.FloatField()),
                ('time_added', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'managed': True,
                'db_table': 'buckminster1',
            },
        ),
        migrations.CreateModel(
            name='Buckminster2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temp', models.FloatField()),
                ('lux', models.FloatField()),
                ('rel_humidity', models.FloatField()),
                ('time_added', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'managed': True,
                'db_table': 'buckminster2',
            },
        ),
        migrations.CreateModel(
            name='Floor1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_added', models.DateTimeField(auto_now_add=True)),
                ('no_of_ppl', models.IntegerField()),
            ],
            options={
                'managed': True,
                'db_table': 'floor1',
            },
        ),
        migrations.CreateModel(
            name='Floor3',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_added', models.DateTimeField(auto_now_add=True)),
                ('no_of_ppl', models.IntegerField()),
            ],
            options={
                'managed': True,
                'db_table': 'floor3',
            },
        ),
        migrations.CreateModel(
            name='Floor4',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_added', models.DateTimeField(auto_now_add=True)),
                ('no_of_ppl', models.IntegerField()),
            ],
            options={
                'managed': True,
                'db_table': 'floor4',
            },
        ),
        migrations.CreateModel(
            name='Gutenberg1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temp', models.FloatField()),
                ('lux', models.FloatField()),
                ('rel_humidity', models.FloatField()),
                ('time_added', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'managed': True,
                'db_table': 'gutenberg1',
            },
        ),
        migrations.CreateModel(
            name='Gutenberg2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temp', models.FloatField()),
                ('lux', models.FloatField()),
                ('rel_humidity', models.FloatField()),
                ('time_added', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'managed': True,
                'db_table': 'gutenberg2',
            },
        ),
        migrations.CreateModel(
            name='IDC1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temp', models.FloatField()),
                ('lux', models.FloatField()),
                ('rel_humidity', models.FloatField()),
                ('time_added', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'managed': True,
                'db_table': 'idc1',
            },
        ),
        migrations.CreateModel(
            name='MPN1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temp', models.FloatField()),
                ('lux', models.FloatField()),
                ('rel_humidity', models.FloatField()),
                ('time_added', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'managed': True,
                'db_table': 'mpn1',
            },
        ),
        migrations.CreateModel(
            name='SteveJobs1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temp', models.FloatField()),
                ('lux', models.FloatField()),
                ('rel_humidity', models.FloatField()),
                ('time_added', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'managed': True,
                'db_table': 'stevejobs1',
            },
        ),
        migrations.CreateModel(
            name='SteveJobs2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temp', models.FloatField()),
                ('lux', models.FloatField()),
                ('rel_humidity', models.FloatField()),
                ('time_added', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'managed': True,
                'db_table': 'stevejobs2',
            },
        ),
        migrations.RemoveField(
            model_name='idcdata',
            name='no_of_ppl',
        ),
    ]
