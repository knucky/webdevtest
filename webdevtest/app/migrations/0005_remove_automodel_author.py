# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-01 17:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_automodel_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='automodel',
            name='author',
        ),
    ]
