# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-08 10:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category_code',
            field=models.CharField(max_length=10),
        ),
    ]
