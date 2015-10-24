from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from info.models import Info

# Create your models here.
class PublishManager(models.Manager):
    def get_queryset(self):
        return super(PublishManager, self).get_queryset().exclude(
        is_draft=True)


class Article(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=50, default=u'Uncategorized')
    content = models.TextField(blank=True, null=True)
    date_time = models.DateTimeField(auto_now_add=True)
    last_updated_in = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, null=True)
    last_updated_by = models.ForeignKey(User, null=True,
                                        related_name='last_updated_by')
    is_draft = models.BooleanField(default=False)
    published = PublishManager()

    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ('detail', [self.id,]) 

    class Meta:
        ordering = ['-date_time']



