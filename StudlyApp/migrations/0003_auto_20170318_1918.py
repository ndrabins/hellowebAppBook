# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-18 19:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('StudlyApp', '0002_auto_20170318_1704'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SchoolClasses',
            new_name='Course',
        ),
    ]
