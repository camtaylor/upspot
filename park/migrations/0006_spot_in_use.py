# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-04 02:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('park', '0005_spot_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='spot',
            name='in_use',
            field=models.BooleanField(default=False),
        ),
    ]
