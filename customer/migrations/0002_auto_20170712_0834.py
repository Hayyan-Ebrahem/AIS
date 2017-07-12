# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-12 08:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='address',
            field=models.TextField(max_length=20),
        ),
        migrations.AlterField(
            model_name='customer',
            name='code',
            field=models.CharField(max_length=10, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='customer',
            name='name',
            field=models.TextField(max_length=10, unique=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='phone_no',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]
