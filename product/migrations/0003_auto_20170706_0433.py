# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-06 04:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20170704_1633'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['-created_at'], 'verbose_name_plural': 'Categories'},
        ),
        migrations.RemoveField(
            model_name='productcategory',
            name='price',
        ),
    ]
