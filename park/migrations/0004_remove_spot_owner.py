# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-22 18:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('park', '0003_auto_20160221_1426'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='spot',
            name='owner',
        ),
    ]