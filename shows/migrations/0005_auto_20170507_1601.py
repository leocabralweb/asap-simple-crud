# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-07 16:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('shows', '0004_show_published'),
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('start', models.DateTimeField(verbose_name='Start')),
                ('end', models.DateTimeField(blank=True, verbose_name='End')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterModelManagers(
            name='show',
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AddField(
            model_name='schedule',
            name='show',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='schedule', to='shows.Show'),
        ),
    ]
