# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-08 18:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0003_auto_20170708_1837'),
        ('product', '0003_auto_20170708_1341'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pricelistdetial',
            name='price_list_code',
        ),
        migrations.RemoveField(
            model_name='pricelistdetial',
            name='product_code',
        ),
        migrations.DeleteModel(
            name='PriceList',
        ),
        migrations.DeleteModel(
            name='PriceListDetial',
        ),
    ]