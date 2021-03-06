# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-22 13:38
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0013_auto_20171022_2231'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='situation',
        ),
        migrations.AddField(
            model_name='todo',
            name='correspondence_contents',
            field=models.TextField(blank=True, validators=[django.core.validators.MaxLengthValidator(64)], verbose_name='対応内容'),
        ),
        migrations.AddField(
            model_name='todo',
            name='correspondence_situation',
            field=models.TextField(blank=True, validators=[django.core.validators.MaxLengthValidator(64)], verbose_name='対応状況'),
        ),
    ]
