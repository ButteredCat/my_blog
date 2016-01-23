# -*- coding:utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from info.models import Info


class Category(models.Model):
    name = models.CharField(u'分类名称', max_length=50, unique=True)

    def __unicode__(self):
        return self.name
    
    class Meta:
        verbose_name = u'分类'
        verbose_name_plural = u'分类'


class PublishManager(models.Manager):
    def get_queryset(self):
        return super(PublishManager, self).get_queryset().exclude(
            is_draft=True)

    def filter_by_category(self, n):
        return self.get_queryset().filter(
            category=Category.objects.get(name=n))


class Article(models.Model):
    title = models.CharField(u'标题', max_length=100)
    category = models.ForeignKey(Category, verbose_name=u'分类', null=True)
    content = models.TextField(u'正文', blank=True)
    date_time = models.DateTimeField(u'创建时间', auto_now_add=True)
    last_updated_in = models.DateTimeField(u'最近修改于', auto_now=True)
    author = models.ForeignKey(User, verbose_name=u'作者',  null=True)
    last_updated_by = models.ForeignKey(User, verbose_name=u'最近修改', null=True,
                                        related_name='last_updated_by')
    is_draft = models.BooleanField(u'存为草稿', default=False)

    objects = models.Manager()
    published = PublishManager()

    def __unicode__(self):
        return self.title

    def get_url(self):
        host_name = Info.get_solo().host
        path = reverse('detail', kwargs={'pk': self.id})
        return '%s%s' % (host_name, path)

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.id})

    class Meta:
        ordering = ['-date_time']
        verbose_name = u'文章'
        verbose_name_plural = u'文章'

