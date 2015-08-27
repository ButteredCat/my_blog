# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=50, blank=True)),
                ('content', models.TextField(null=True, blank=True)),
                ('date_time', models.DateTimeField(auto_now_add=True)),
                ('last_updated_in', models.DateTimeField(auto_now=True)),
                ('is_draft', models.BooleanField(default=False)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True)),
                ('last_updated_by', models.ForeignKey(related_name='last_updated_by', to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'ordering': ['-date_time'],
            },
        ),
    ]
