# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0003_auto_20151129_2016'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='lyrics',
            field=models.TextField(null=True, blank=True),
        ),
    ]
