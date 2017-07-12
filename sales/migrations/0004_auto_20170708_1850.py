# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-08 18:50
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0003_auto_20170708_1837'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='salesorder',
            name='create_date',
        ),
        migrations.RemoveField(
            model_name='salesorderdetail',
            name='unit_price',
        ),
        migrations.AddField(
            model_name='salesorder',
            name='create_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2017, 7, 8, 18, 50, 10, 475983, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='salesorder',
            name='customer_order_no',
            field=models.TextField(max_length='10'),
        ),
        migrations.AlterField(
            model_name='salesorderdetail',
            name='product_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='product.Product'),
        ),
    ]