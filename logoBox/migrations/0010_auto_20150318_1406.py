# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('logoBox', '0009_auto_20150318_1356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='post_id_rate',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
