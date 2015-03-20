# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('logoBox', '0014_auto_20150318_1453'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='picture',
            field=models.ImageField(upload_to=b'poster_images', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='lastActive',
            field=models.DateTimeField(default=datetime.date(2015, 3, 20)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='timeCreated',
            field=models.DateTimeField(default=datetime.date(2015, 3, 20)),
            preserve_default=True,
        ),
    ]
