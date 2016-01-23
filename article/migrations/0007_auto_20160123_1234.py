# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0006_auto_20160123_1147'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': '\u5206\u7c7b', 'verbose_name_plural': '\u5206\u7c7b'},
        ),
        migrations.AlterField(
            model_name='article',
            name='author',
            field=models.ForeignKey(verbose_name='\u4f5c\u8005', to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.ForeignKey(verbose_name='\u5206\u7c7b', to='article.Category', null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='last_updated_by',
            field=models.ForeignKey(related_name='last_updated_by', verbose_name='\u6700\u8fd1\u4fee\u6539', to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='last_updated_in',
            field=models.DateTimeField(auto_now=True, verbose_name='\u6700\u540e\u4fee\u6539\u4e8e'),
        ),
    ]
