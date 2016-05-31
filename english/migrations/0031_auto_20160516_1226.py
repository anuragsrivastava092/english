# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-16 06:56
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('english', '0030_article_article_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='bookmark_attempted',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('response', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='bookmark_questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=400)),
                ('choice1', models.CharField(max_length=300)),
                ('choice2', models.CharField(max_length=300)),
                ('choice3', models.CharField(max_length=300)),
                ('choice4', models.CharField(max_length=300)),
                ('right_choice', models.CharField(choices=[('', '---------'), ('1', 'choice1'), ('2', 'choice2'), ('3', 'choice3'), ('4', 'choice4')], default='', max_length=2)),
                ('word_used', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='english.bookmark')),
            ],
        ),
        migrations.AlterField(
            model_name='sample_question',
            name='paragraph_pos',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='sample_question',
            name='sentence_pos',
            field=models.IntegerField(blank=True),
        ),
        migrations.AddField(
            model_name='bookmark_attempted',
            name='question_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='english.bookmark_questions'),
        ),
        migrations.AddField(
            model_name='bookmark_attempted',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
