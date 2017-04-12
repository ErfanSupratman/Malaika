# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-12 09:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Diagnose',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('code', models.IntegerField(default=0, unique=True)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_number', models.IntegerField(default=0, unique=True)),
                ('room_type', models.CharField(choices=[('Maternity', 'Maternity'), ('General', 'General'), ('Ward', 'Ward')], max_length=200)),
            ],
        ),
    ]
