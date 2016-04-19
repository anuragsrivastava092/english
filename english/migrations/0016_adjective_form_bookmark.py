# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-28 05:39
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('english', '0015_dictionary'),
    ]

    operations = [
        migrations.CreateModel(
            name='adjective_form',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_form', models.CharField(max_length=20)),
                ('second_form', models.CharField(max_length=20)),
                ('third_form', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='bookmark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('word', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='english.dictionary')),
            ],
        ),
    ]
