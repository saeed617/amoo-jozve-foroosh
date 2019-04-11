# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-11 15:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('advertise', '0003_auto_20190411_1638'),
    ]

    operations = [
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='university name')),
            ],
            options={
                'verbose_name_plural': 'Universities',
            },
        ),
        migrations.AlterModelOptions(
            name='county',
            options={'verbose_name_plural': 'Counties'},
        ),
        migrations.AddField(
            model_name='university',
            name='county',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='universities', to='advertise.County', verbose_name='County'),
        ),
        migrations.AddField(
            model_name='advertise',
            name='university',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='advertise.University', verbose_name='University'),
        ),
    ]
