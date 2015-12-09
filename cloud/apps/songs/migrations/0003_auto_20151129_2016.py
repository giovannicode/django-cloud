# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import apps.songs.models


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0002_song_artist'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='name',
            field=models.CharField(default='song name', max_length=60),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='song',
            name='soundfile',
            field=models.FileField(),
        ),
    ]
