# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('logoBox', '0003_auto_20150306_1536'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(default=b'cat', max_length=64),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='poster_id',
            field=models.CharField(default=b'1', max_length=64),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='rating',
            name='post_id_rate',
            field=models.ForeignKey(to='logoBox.Post', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='rating',
            name='poster_id_rate',
            field=models.ForeignKey(to='logoBox.UserProfile', blank=True),
            preserve_default=True,
        ),
    ]
