# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-21 01:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_auto_20170116_0847'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChartLvl1_DayNew',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('light_duration', models.FloatField()),
                ('nobody_present', models.FloatField()),
                ('light_day', models.FloatField()),
                ('comp_day', models.FloatField()),
                ('ac_day', models.FloatField()),
                ('totalkWh_day', models.FloatField()),
                ('totalBill_day', models.DecimalField(decimal_places=2, max_digits=8)),
            ],
            options={
                'db_table': 'ChartL1_DayNew',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ChartLvl1_Min',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('acOn', models.FloatField()),
                ('userMins', models.FloatField()),
                ('comp_day', models.FloatField()),
                ('ac_day', models.FloatField()),
                ('totalkWh_day', models.FloatField()),
                ('totalBill_day', models.DecimalField(decimal_places=2, max_digits=8)),
            ],
            options={
                'db_table': 'ChartL1_Min',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ChartLvl1_Yr',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('light_duration_Yr', models.FloatField()),
                ('nobodyDuration_Yr', models.FloatField()),
                ('totallight_Yr', models.FloatField()),
                ('totalac_Yr', models.FloatField()),
                ('totalcomp_Yr', models.FloatField()),
                ('totalkWh_Yr', models.FloatField()),
                ('totalBill_Yr', models.DecimalField(decimal_places=2, max_digits=8)),
                ('estlight_duration_Yr', models.DecimalField(decimal_places=2, max_digits=8)),
                ('estnobodyDuration_Yr', models.DecimalField(decimal_places=2, max_digits=8)),
                ('esttotallight_Yr', models.DecimalField(decimal_places=2, max_digits=8)),
                ('esttotalac_Yr', models.DecimalField(decimal_places=2, max_digits=8)),
                ('esttotalcomp_Yr', models.DecimalField(decimal_places=2, max_digits=8)),
                ('esttotalkWh_Yr', models.DecimalField(decimal_places=2, max_digits=8)),
                ('esttotalBill_Yr', models.DecimalField(decimal_places=2, max_digits=8)),
            ],
            options={
                'db_table': 'ChartL1_Yr',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='InfoL1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('annualCO2', models.IntegerField()),
                ('roundSg', models.IntegerField()),
                ('numTree2Plant', models.IntegerField()),
                ('tnumTreeinYr', models.IntegerField()),
            ],
            options={
                'db_table': 'InfoL1',
                'managed': True,
            },
        ),
        migrations.DeleteModel(
            name='Buckminster1',
        ),
        migrations.DeleteModel(
            name='Buckminster2',
        ),
        migrations.DeleteModel(
            name='Floor1',
        ),
        migrations.DeleteModel(
            name='Floor3',
        ),
        migrations.DeleteModel(
            name='Floor4',
        ),
        migrations.DeleteModel(
            name='Gutenberg1',
        ),
        migrations.DeleteModel(
            name='Gutenberg2',
        ),
        migrations.DeleteModel(
            name='IDC1',
        ),
        migrations.DeleteModel(
            name='MPN1',
        ),
        migrations.DeleteModel(
            name='SteveJobs1',
        ),
        migrations.DeleteModel(
            name='SteveJobs2',
        ),
    ]