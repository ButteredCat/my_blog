# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0006_auto_20151211_1223'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='info',
            options={'verbose_name': '\u7f51\u7ad9\u914d\u7f6e', 'verbose_name_plural': '\u7f51\u7ad9\u914d\u7f6e'},
        ),
        migrations.AlterField(
            model_name='info',
            name='description',
            field=models.CharField(default=b'My Django Blog', max_length=255, verbose_name='\u7ad9\u70b9\u526f\u6807\u9898', blank=True),
        ),
        migrations.AlterField(
            model_name='info',
            name='duoshuo',
            field=models.CharField(max_length=31, verbose_name='\u591a\u8bf4\u8d26\u53f7', blank=True),
        ),
        migrations.AlterField(
            model_name='info',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='\u8054\u7cfb\u90ae\u7bb1', blank=True),
        ),
        migrations.AlterField(
            model_name='info',
            name='host',
            field=models.URLField(verbose_name='\u9996\u9875\u7f51\u5740', blank=True),
        ),
        migrations.AlterField(
            model_name='info',
            name='name',
            field=models.CharField(default='My Blog', max_length=255, verbose_name='\u7ad9\u70b9\u540d\u79f0'),
        ),
    ]
