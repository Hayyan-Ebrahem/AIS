# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-29 12:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customer', '__first__'),
        ('product', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='SalesOrder',
            fields=[
                ('sale_order_id', models.AutoField(primary_key=True, serialize=False)),
                ('customer_order_no', models.IntegerField()),
                ('customer_order_date', models.DateTimeField()),
                ('payment_term', models.TextField(choices=[('PIA', 'Payment in advance'), ('EOM', 'End of the month'), ('CWO', 'Cash with order')], default='EOM', max_length=50)),
                ('create_date', models.DateTimeField()),
                ('status', models.TextField(choices=[('WIP', 'working in process'), ('INVOICED', 'invoiced')], default='WIP')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='SalesOrderDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_unit', models.IntegerField()),
                ('unit_price', models.IntegerField()),
                ('ordered_qty', models.DecimalField(decimal_places=2, max_digits=5)),
                ('delivered_qty', models.DecimalField(decimal_places=2, max_digits=5)),
                ('note', models.TextField(max_length=200)),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.Product')),
                ('sales_order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lines', to='sales.SalesOrder')),
            ],
        ),
    ]
