# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-21 19:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0003_auto_20160921_2340'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='relation',
            name='participant_id',
        ),
        migrations.RemoveField(
            model_name='relation',
            name='team_id',
        ),
        migrations.DeleteModel(
            name='Relation',
        ),
    ]
