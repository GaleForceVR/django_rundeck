# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('efforts', '0002_auto_20150808_1252'),
    ]

    operations = [
        migrations.AddField(
            model_name='route',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='route',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='split',
            name='split_time',
            field=models.DurationField(),
        ),
    ]
