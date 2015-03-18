# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('logoBox', '0008_auto_20150317_1838'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='lastActive',
            field=models.DateTimeField(default=datetime.date(2015, 3, 18)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='timeCreated',
            field=models.DateTimeField(default=datetime.date(2015, 3, 18)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='rating',
            name='post_id_rate',
            field=models.CharField(default=b'1', max_length=64),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='rating',
            name='poster_id_rate',
            field=models.CharField(default=b'1', max_length=64),
            preserve_default=True,
        ),
    ]
