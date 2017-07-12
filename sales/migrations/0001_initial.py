# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-11 20:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0001_initial'),
        ('customer', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='SalesOrder',
            fields=[
                ('sale_order_id', models.AutoField(primary_key=True, serialize=False)),
                ('customer_order_no', models.TextField(max_length='10')),
                ('customer_order_date', models.DateTimeField()),
                ('payment_term', models.CharField(choices=[('PIA', 'Payment in advance'), ('EOM', 'End of the month'), ('CWO', 'Cash with order')], default='EOM', max_length=5)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('WIP', 'working in process'), ('INVOICED', 'invoiced')], default='WIP', max_length=5)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='customer.Customer')),
            ],
            options={
                'ordering': ['-create_at'],
            },
        ),
        migrations.CreateModel(
            name='SalesOrderDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordered_qty', models.IntegerField()),
                ('delivered_qty', models.IntegerField()),
                ('note', models.TextField(blank=True, max_length=20)),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='sales.SalesOrder')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='product.Product')),
            ],
        ),
    ]
