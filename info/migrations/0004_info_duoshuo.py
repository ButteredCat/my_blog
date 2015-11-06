# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0003_delete_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='info',
            name='duoshuo',
            field=models.CharField(default='butteredcat', max_length=31),
            preserve_default=False,
        ),
    ]
