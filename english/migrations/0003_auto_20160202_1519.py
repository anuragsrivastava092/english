# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-02 09:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('english', '0002_auto_20160201_1853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='right_choice',
            field=models.CharField(choices=[('', '---------'), (models.CharField(max_length=50), 'choice1'), (models.CharField(max_length=50), 'choice2'), (models.CharField(max_length=50), 'choice3'), (models.CharField(max_length=50), 'choice4')], default='', max_length=2),
        ),
    ]