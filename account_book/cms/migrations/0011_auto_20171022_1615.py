# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-22 07:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0010_auto_20170918_1034'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='deadline',
            field=models.DateTimeField(blank=True, null=True, verbose_name='期限'),
        ),
        migrations.AlterField(
            model_name='todo',
            name='priority',
            field=models.IntegerField(choices=[(1, 'Immediate'), (2, 'Urgent'), (3, 'High'), (4, 'Normal'), (5, 'Low')], default=4, verbose_name='優先順位'),
        ),
    ]
