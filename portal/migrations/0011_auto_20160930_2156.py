# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-30 16:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0010_participant_is_paid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='contact',
            field=models.CharField(max_length=13),
        ),
    ]
