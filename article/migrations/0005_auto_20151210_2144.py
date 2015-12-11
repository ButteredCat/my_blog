# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0004_article_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='content',
            field=models.TextField(default=datetime.datetime(2015, 12, 10, 21, 44, 51, 576157), blank=True),
            preserve_default=False,
        ),
    ]
