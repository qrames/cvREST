# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2018-12-10 10:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='technologie',
            name='progress',
            field=models.PositiveSmallIntegerField(),
        ),
    ]
