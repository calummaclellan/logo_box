# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('logoBox', '0015_auto_20150320_1335'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'get_latest_by': 'timeCreated'},
        ),
        migrations.AlterField(
            model_name='post',
            name='lastActive',
            field=models.DateTimeField(auto_now=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='timeCreated',
            field=models.DateTimeField(auto_now_add=True),
            preserve_default=True,
        ),
    ]
