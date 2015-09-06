# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('efforts', '0006_auto_20150809_1458'),
    ]

    operations = [
        migrations.AddField(
            model_name='effort',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='effort',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='split',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='split',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
