# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-28 10:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('english', '0033_auto_20160522_1053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sample_performance',
            name='paragraph_pos',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='sample_performance',
            name='sentence_pos',
            field=models.IntegerField(null=True),
        ),
    ]