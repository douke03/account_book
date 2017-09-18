# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-17 16:25
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0008_auto_20170918_0122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='title',
            field=models.TextField(validators=[django.core.validators.MaxLengthValidator(32)], verbose_name='タイトル'),
        ),
    ]
