# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-19 21:18
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0003_auto_20170417_1207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='dob',
            field=models.DateField(default=datetime.date(2017, 4, 19)),
        ),
    ]
