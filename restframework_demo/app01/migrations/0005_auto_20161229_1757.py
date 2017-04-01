# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-29 09:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0004_auto_20161229_1756'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='sign',
        ),
        migrations.AddField(
            model_name='author',
            name='sign',
            field=models.CharField(choices=[('yes', 'yes'), ('no', 'no')], default='no', max_length=32, verbose_name='签约与否'),
        ),
    ]
