# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-16 07:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app02', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sales',
            name='country_code',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sales', to='app02.ExportCountries', verbose_name='出口国编码'),
        ),
        migrations.AlterField(
            model_name='salesinfo',
            name='product_code',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sales_info', to='app02.Products', verbose_name='商品编码'),
        ),
        migrations.AlterField(
            model_name='salesinfo',
            name='sale_code',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sales_info', to='app02.Sales', verbose_name='报表编码'),
        ),
    ]
