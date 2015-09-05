# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('efforts', '0003_auto_20150809_1949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='route',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='route',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
