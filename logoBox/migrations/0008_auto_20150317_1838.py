# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('logoBox', '0007_auto_20150317_1834'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rating',
            name='blank',
        ),
        migrations.AddField(
            model_name='rating',
            name='post_id_rate',
            field=models.ForeignKey(default=b'', to='logoBox.Post'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='rating',
            name='poster_id_rate',
            field=models.ForeignKey(default=b'', to='logoBox.UserProfile'),
            preserve_default=True,
        ),
    ]
