# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('efforts', '0009_auto_20150809_1653'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='effort',
            name='effort_date',
        ),
    ]
