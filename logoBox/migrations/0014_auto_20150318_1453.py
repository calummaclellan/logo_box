# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('logoBox', '0013_auto_20150318_1439'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='post_id_rate',
            field=models.CharField(default=b'1', max_length=64),
            preserve_default=True,
        ),
    ]
