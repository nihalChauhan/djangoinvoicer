# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-05 14:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20170605_1124'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='inventory',
            field=models.IntegerField(default=0),
        ),
    ]
