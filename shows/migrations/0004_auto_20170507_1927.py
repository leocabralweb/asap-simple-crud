# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-07 19:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shows', '0003_show_duration_squashed_0005_auto_20170507_1601'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='show',
            name='card_original',
        ),
        migrations.RemoveField(
            model_name='show',
            name='logo_original',
        ),
        migrations.AlterField(
            model_name='schedule',
            name='end',
            field=models.DateTimeField(blank=True, help_text='Leave blank to automatic fill.', verbose_name='End'),
        ),
    ]
