# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0005_auto_20160227_1545'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(null=True, upload_to='portfolio-featured', blank=True),
        ),
        migrations.AlterField(
            model_name='projectimage',
            name='image',
            field=models.ImageField(upload_to='porfolio-images'),
        ),
    ]
