# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-07 00:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('albulms', '0002_albulm_artist'),
        ('songs', '0005_song_genre'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='albulm',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='albulms.Albulm'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='song',
            name='track_number',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
