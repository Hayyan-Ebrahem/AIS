# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-30 21:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=42),
        ),
    ]
