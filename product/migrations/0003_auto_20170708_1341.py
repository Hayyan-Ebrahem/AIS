# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-08 13:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20170708_1337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pricelistdetial',
            name='price_list_code',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='price_code', to='product.PriceList'),
        ),
        migrations.AlterField(
            model_name='pricelistdetial',
            name='product_code',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product', to='product.Product'),
        ),
    ]
