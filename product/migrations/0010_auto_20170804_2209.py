# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-04 22:09
from __future__ import unicode_literals

from django.db import migrations
import product.managers


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0009_auto_20170804_1711'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='product',
            managers=[
                ('objects', product.managers.ProductManager()),
            ],
        ),
    ]