# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('efforts', '0008_auto_20150809_1509'),
    ]

    operations = [
        migrations.AddField(
            model_name='effort',
            name='effort_date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='effort',
            name='effort_time',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
