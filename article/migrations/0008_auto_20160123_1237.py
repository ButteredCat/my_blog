# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0007_auto_20160123_1234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='last_updated_in',
            field=models.DateTimeField(auto_now=True, verbose_name='\u6700\u8fd1\u4fee\u6539\u4e8e'),
        ),
    ]
