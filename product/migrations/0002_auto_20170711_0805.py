# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-11 08:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='categories',
            field=models.ManyToManyField(to='product.Category'),
        ),
    ]
