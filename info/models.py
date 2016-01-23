# -*- coding:utf-8 -*-
from django.db import models

from solo.models import SingletonModel

# Create your models here.
class Info(SingletonModel):
    name = models.CharField(u'站点名称', max_length=255, default=u'My Blog')
    description = models.CharField(u'站点副标题', max_length=255, blank=True, default='My Django Blog')
    host = models.URLField(u'首页网址', blank=True)
    email = models.EmailField(u'联系邮箱', blank=True)
    duoshuo = models.CharField(u'多说账号', max_length=31, blank=True)

    def __unicode__(self):
        return u"Site Information"

    class Meta:
        verbose_name = u'网站配置'
        verbose_name_plural = u'网站配置'

