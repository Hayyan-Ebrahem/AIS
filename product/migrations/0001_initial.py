# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-26 08:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('category_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Categories',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='PriceList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='PriceListDetials',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, unique=True)),
                ('slug', models.SlugField(help_text='Unique value for product page URL, created from name.', max_length=255, unique=True)),
                ('code', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('categories', models.ManyToManyField(to='product.Category')),
            ],
            options={
                'ordering': ['-price'],
            },
        ),
    ]
