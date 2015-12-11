# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0005_auto_20151210_2144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='host',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='info',
            name='name',
            field=models.CharField(default='My Blog', max_length=255),
        ),
    ]
