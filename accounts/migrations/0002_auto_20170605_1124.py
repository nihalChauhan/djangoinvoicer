# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-05 11:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='group',
        ),
        migrations.AddField(
            model_name='product',
            name='group',
            field=models.ManyToManyField(blank=True, to='accounts.ProductGroup'),
        ),
    ]
