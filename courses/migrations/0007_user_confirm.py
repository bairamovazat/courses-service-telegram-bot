# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-12-19 09:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0006_auto_20181219_1149'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='confirm',
            field=models.BooleanField(default=False),
        ),
    ]