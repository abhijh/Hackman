# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-27 19:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0007_auto_20160922_0049'),
    ]

    operations = [
        migrations.AddField(
            model_name='participant',
            name='is_approved',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
