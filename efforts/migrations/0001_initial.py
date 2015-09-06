# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Effort',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('total_time', models.DurationField(default=datetime.timedelta(0))),
                ('total_distance', models.DecimalField(max_digits=5, decimal_places=2)),
            ],
        ),
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('distance', models.DecimalField(max_digits=5, decimal_places=2)),
                ('location', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Split',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('distance', models.DecimalField(max_digits=5, decimal_places=2)),
                ('split_time', models.DurationField(default=datetime.timedelta(0))),
                ('effort', models.ForeignKey(to='efforts.Effort')),
            ],
        ),
        migrations.AddField(
            model_name='effort',
            name='route',
            field=models.ForeignKey(to='efforts.Route'),
        ),
        migrations.AddField(
            model_name='effort',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
