# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('logoBox', '0010_auto_20150318_1406'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='post_id_rate',
            field=models.ForeignKey(to='logoBox.Post'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='rating',
            name='poster_id_rate',
            field=models.ForeignKey(to='logoBox.UserProfile'),
            preserve_default=True,
        ),
    ]
