# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('logoBox', '0011_auto_20150318_1410'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='post_id_rate',
            field=models.ForeignKey(to='logoBox.Post', db_index=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='rating',
            name='poster_id_rate',
            field=models.CharField(default=b'1', max_length=64),
            preserve_default=True,
        ),
    ]
