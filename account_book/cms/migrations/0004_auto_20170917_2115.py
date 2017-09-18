# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-17 12:15
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0003_todo_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='priority',
            field=models.IntegerField(default=3, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)], verbose_name='優先順位'),
        ),
        migrations.AddField(
            model_name='todo',
            name='situation',
            field=models.CharField(blank=True, max_length=32, verbose_name='対応状況'),
        ),
        migrations.AlterField(
            model_name='todo',
            name='title',
            field=models.CharField(max_length=32, verbose_name='タイトル'),
        ),
    ]
