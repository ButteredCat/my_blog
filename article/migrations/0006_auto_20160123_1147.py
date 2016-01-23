# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0005_auto_20151210_2144'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-date_time'], 'verbose_name': '\u6587\u7ae0', 'verbose_name_plural': '\u6587\u7ae0'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': '\u6587\u7ae0\u5206\u7c7b', 'verbose_name_plural': '\u6587\u7ae0\u5206\u7c7b'},
        ),
        migrations.AlterField(
            model_name='article',
            name='content',
            field=models.TextField(verbose_name='\u6b63\u6587', blank=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='date_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4'),
        ),
        migrations.AlterField(
            model_name='article',
            name='is_draft',
            field=models.BooleanField(default=False, verbose_name='\u5b58\u4e3a\u8349\u7a3f'),
        ),
        migrations.AlterField(
            model_name='article',
            name='last_updated_in',
            field=models.DateTimeField(auto_now=True, verbose_name='\u6700\u540e\u66f4\u65b0\u4e8e'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=100, verbose_name='\u6807\u9898'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(unique=True, max_length=50, verbose_name='\u5206\u7c7b\u540d\u79f0'),
        ),
    ]
