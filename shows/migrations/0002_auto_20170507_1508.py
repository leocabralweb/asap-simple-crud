# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-07 15:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shows', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='show',
            old_name='card',
            new_name='card_original',
        ),
        migrations.RenameField(
            model_name='show',
            old_name='logo',
            new_name='logo_original',
        ),
    ]
