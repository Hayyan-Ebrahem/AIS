# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-30 21:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20170630_1401'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productcategory',
            name='price',
            field=models.IntegerField(),
        ),
    ]
