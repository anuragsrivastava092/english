# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-13 12:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('english', '0022_auto_20160413_1449'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sample_question',
            name='word',
            field=models.CharField(blank=True, max_length=301),
        ),
    ]
