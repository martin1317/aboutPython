# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-29 09:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0003_auto_20161227_2354'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='sign',
            field=models.CharField(choices=[('yes', 'yes'), ('no', 'no')], default='no', max_length=32, verbose_name='签约与否'),
        ),
        migrations.AlterField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', to='app01.Publisher'),
        ),
    ]
