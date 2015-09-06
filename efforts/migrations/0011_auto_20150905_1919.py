# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('efforts', '0010_remove_effort_effort_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='effort',
            name='route',
            field=models.ForeignKey(to='routes.Route'),
        ),
        migrations.DeleteModel(
            name='Route',
        ),
    ]
