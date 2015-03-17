# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('logoBox', '0006_rating_blank'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rating',
            name='post_id_rate',
        ),
        migrations.RemoveField(
            model_name='rating',
            name='poster_id_rate',
        ),
    ]
