# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-06-12 20:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_auto_20190520_0342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='active',
            field=models.BooleanField(default=False),
        ),
    ]
