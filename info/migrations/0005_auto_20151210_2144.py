# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0004_info_duoshuo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='description',
            field=models.CharField(default=b'My Django Blog', max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='info',
            name='duoshuo',
            field=models.CharField(max_length=31, blank=True),
        ),
        migrations.AlterField(
            model_name='info',
            name='email',
            field=models.EmailField(max_length=254, blank=True),
        ),
        migrations.AlterField(
            model_name='info',
            name='name',
            field=models.CharField(default='My Blog', max_length=255, blank=True),
        ),
    ]
