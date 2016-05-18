# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0009_auto_20160517_2340'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='short_description',
            field=models.CharField(default=datetime.datetime(2016, 5, 17, 20, 56, 24, 759177, tzinfo=utc), max_length=300),
            preserve_default=False,
        ),
    ]
