# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-04 08:04
from __future__ import unicode_literals

from django.db import migrations
import product.managers


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_auto_20170803_2255'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='product',
            managers=[
                ('objects', product.managers.ProductManager()),
            ],
        ),
    ]