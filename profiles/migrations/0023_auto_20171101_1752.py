# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-11-01 16:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0022_auto_20171101_1455'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(blank=True, help_text='A label for the URL config', max_length=31, unique=True),
        ),
    ]
