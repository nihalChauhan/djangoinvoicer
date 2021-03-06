# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-13 12:31
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_product_inventory'),
    ]

    operations = [
        migrations.CreateModel(
            name='BilledProducts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('quantity', models.IntegerField(default=0)),
                ('price', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Bills',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoice_date', models.DateField(default=datetime.datetime(2017, 6, 13, 12, 31, 20, 917044, tzinfo=utc))),
                ('due_date', models.DateField(default=datetime.datetime(2017, 6, 13, 12, 31, 20, 917130, tzinfo=utc))),
                ('to', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='product',
            name='group',
        ),
        migrations.AddField(
            model_name='productgroup',
            name='products',
            field=models.ManyToManyField(blank=True, to='accounts.Product'),
        ),
        migrations.AddField(
            model_name='billedproducts',
            name='bill',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Bills'),
        ),
    ]
