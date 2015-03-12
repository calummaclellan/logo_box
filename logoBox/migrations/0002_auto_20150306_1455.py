# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('logoBox', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='poster_id',
            field=models.ForeignKey(to='logoBox.UserProfile', unique=True),
        ),
    ]
