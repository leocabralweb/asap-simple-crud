# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-07 15:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shows', '0003_show_duration'),
    ]

    operations = [
        migrations.AddField(
            model_name='show',
            name='published',
            field=models.BooleanField(default=False, verbose_name='Published'),
        ),
    ]