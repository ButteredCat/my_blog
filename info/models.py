from django.db import models

from solo.models import SingletonModel

# Create your models here.
class Info(SingletonModel):
    name = models.CharField(max_length=255, default=u'My Blog')
    description = models.CharField(max_length=255, blank=True, default='My Django Blog')
    host = models.URLField(blank=True)
    email = models.EmailField(blank=True)
    duoshuo = models.CharField(max_length=31, blank=True)

    def __unicode__(self):
        return u"Site Information"

