# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-06 13:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0009_auto_20161106_1445'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='image',
            field=models.ImageField(upload_to='images'),
        ),
    ]