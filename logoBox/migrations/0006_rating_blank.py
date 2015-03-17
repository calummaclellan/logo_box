# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('logoBox', '0005_auto_20150317_1825'),
    ]

    operations = [
        migrations.AddField(
            model_name='rating',
            name='blank',
            field=models.CharField(default=b'1', max_length=64),
            preserve_default=True,
        ),
    ]
