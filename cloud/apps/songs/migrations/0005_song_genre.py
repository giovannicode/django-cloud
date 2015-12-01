# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('genres', '0001_initial'),
        ('songs', '0004_song_lyrics'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='genre',
            field=models.ForeignKey(default=1, to='genres.Genre'),
            preserve_default=False,
        ),
    ]
